# Generated by Django 3.2.6 on 2021-08-25 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_homepage_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='highlighted_campaign',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='highlighted_description',
            field=models.TextField(null=True),
        ),
    ]