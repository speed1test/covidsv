# Generated by Django 2.2.6 on 2020-07-11 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0002_departamento_municipio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='idDepartamento',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='municipio',
            name='idMunicipio',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
