# Generated by Django 2.2.6 on 2020-07-12 07:36

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('covid', '0003_auto_20200711_2346'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Labatorista',
            new_name='Laboratorista',
        ),
    ]