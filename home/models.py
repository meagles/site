from home.views import EmailFormView
from django.db import models
from datetime import datetime
from wagtail.core.models import Page
from django.shortcuts import render
from wagtail.admin.edit_handlers import FieldPanel
from events.models import Event
from news.models import NewsPage
from wagtail.core.fields import RichTextField


class HomePage(Page):
    banner_title = models.CharField(max_length=100, blank=False, null=True)
    mission_statement = models.TextField(null=True)
    values_statement = models.TextField(null=True)
    highlighted_campaign = models.CharField(max_length=100, blank=False, null=True)
    highlighted_description = RichTextField(blank=False, null=True)
    action_network_embed_api_endpoint = models.URLField(blank=True, null=True)

    max_count = 1

    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("mission_statement"),
        FieldPanel("values_statement"),
        FieldPanel("highlighted_campaign"),
        FieldPanel("highlighted_description"),
    ]

    def get_context(self, request):
        context = super(HomePage, self).get_context(request)
        context["events"] = (
            Event.objects.filter(start__gte=datetime.today().date())
            .exclude(title__icontains="members only")
            .order_by("start")[:4]
        )
        context["update"] = NewsPage.objects.all().order_by("-date")[0]
        return context

    def serve(self, request):
        if request.method != "POST":
            return super().serve(request)

        request.session["email"] = request.POST["email"]
        return EmailFormView.as_view()(request)
