# Generated by Django 3.1.8 on 2021-04-13 21:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_auto_20210209_1119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='start_time',
        ),
        migrations.AddField(
            model_name='event',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 13, 16, 22, 23, 17290)),
            preserve_default=False,
        ),
    ]