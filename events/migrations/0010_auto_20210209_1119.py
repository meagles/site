# Generated by Django 3.1.6 on 2021-02-09 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0009_auto_20200418_1749"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="title",
            field=models.CharField(max_length=200),
        ),
    ]
