# Generated by Django 2.2.6 on 2020-07-11 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='rol',
            field=models.IntegerField(default=2),
        ),
    ]
