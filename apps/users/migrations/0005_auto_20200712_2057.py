# Generated by Django 2.2.6 on 2020-07-12 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_dui'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dui',
            field=models.CharField(max_length=9),
        ),
    ]
