# Generated by Django 3.2.6 on 2021-08-31 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('committees', '0031_person_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='committeepage',
            name='name',
        ),
    ]
