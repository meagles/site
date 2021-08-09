# Generated by Django 3.1.8 on 2021-08-09 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_user_is_member'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_member',
        ),
        migrations.AddField(
            model_name='user',
            name='membership',
            field=models.TextField(blank=True, choices=[('Active', 'Active'), ('In Arrears', 'In Arrears'), ('LAPSED', 'Lapsed'), ('None', 'None')], null=True),
        ),
    ]