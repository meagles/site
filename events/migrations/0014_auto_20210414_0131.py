# Generated by Django 3.1.8 on 2021-04-14 06:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_remove_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apicalls',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2, 1, 1, 1, 1, 2)),
        ),
    ]
