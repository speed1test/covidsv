# Generated by Django 2.2.6 on 2020-07-13 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0005_paciente'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='apellido_paciente',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paciente',
            name='dui',
            field=models.CharField(default=123456789, max_length=9),
            preserve_default=False,
        ),
    ]