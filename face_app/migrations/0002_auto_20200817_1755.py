# Generated by Django 3.0.8 on 2020-08-17 14:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='regno',
            field=models.CharField(max_length=30, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_registration_number', message='Registration Number entered was not correctly formated!!', regex='^[A-Z]{3}/[A-Z]{3}/\\d{2}/\\d{5}$')]),
        ),
    ]
