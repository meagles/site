from django.db import models
from stl_dsa.users.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.search import index
from wagtailmenus.models import MenuPage
from datetime import datetime


class Person(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.SET_NULL)
    phone = PhoneNumberField(null=True, blank=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Person(user=instance).save()

    def __str__(self):
        if self.user:
            return (self.user.first_name or "") + " " + (self.user.last_name or "")


class CommitteePage(Page):
    parent_page_types = ["CommitteesPage"]
    subpage_types = []

    COMMITTEE = "CT"
    WORKING_GROUP = "WG"
    CAUCUS = "CU"
    PRIORITY = "PR"
    FORMATION_CHOICES = [
        (COMMITTEE, "Committee"),
        (WORKING_GROUP, "Working Group"),
        (CAUCUS, "Caucus"),
        (PRIORITY, "Priority"),
    ]

    description = RichTextField()
    formation_type = models.CharField(
        max_length=2, choices=FORMATION_CHOICES, default=""
    )
    leader = models.ForeignKey(
        Person,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="committee_leader",
    )
    leader_name = models.CharField(max_length=30, null=True)
    email = models.EmailField()
    people = models.ManyToManyField(Person, related_name="committee_member", blank=True)
    sign_up_form_endpoint = models.TextField(null=True, blank=True)

    search_fields = Page.search_fields + [index.SearchField("description")]

    content_panels = Page.content_panels + [
        FieldPanel("formation_type"),
        FieldPanel("description"),
        FieldPanel("leader_name"),
        FieldPanel("email"),
        FieldPanel("sign_up_form_endpoint"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context["upcoming_events"] = list(self.events.filter(start__gt=datetime.now()))
        # embed_code = embeds["embed_standard_layout_only_styles"]
        # context["embed_code"] = embed_code

        return context

    def __str__(self):
        return self.title.title() + " " + self.get_formation_type_display()


class CommitteesPage(MenuPage):
    subpage_types = ["CommitteePage"]
    description = RichTextField(null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("description"),
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        committees = CommitteePage.objects.all().order_by("title")
        context["committees"] = committees

        return context


class ResourcesPage(Page):
    resources = StreamField(
        [
            (
                "resource",
                blocks.StreamBlock(
                    [
                        ("resource_name", blocks.CharBlock()),
                        ("information", blocks.RichTextBlock()),
                        (
                            "structured_info_block",
                            blocks.StreamBlock(
                                [
                                    ("heading", blocks.CharBlock()),
                                    ("body", blocks.RichTextBlock()),
                                ]
                            ),
                        ),
                    ]
                ),
            )
        ]
    )
    content_panels = Page.content_panels + [
        StreamFieldPanel("resources"),
    ]
