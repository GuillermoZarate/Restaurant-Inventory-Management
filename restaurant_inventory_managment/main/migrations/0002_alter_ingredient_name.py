# Generated by Django 4.2.6 on 2023-11-21 13:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=100, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_name', message='El nombre solo puede contener letras y espacios.', regex='^[a-zA-Z ]+$')]),
        ),
    ]