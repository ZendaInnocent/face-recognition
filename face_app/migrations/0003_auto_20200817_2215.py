# Generated by Django 3.0.8 on 2020-08-17 19:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face_app', '0002_auto_20200817_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phoneNumber',
            field=models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(message='Phone number entered was not correctly formated!!', regex='^\\+?1?\\d{10,15}$')]),
        ),
        migrations.AlterField(
            model_name='student',
            name='regno',
            field=models.CharField(max_length=16, unique=True, validators=[django.core.validators.RegexValidator(message='Registration Number entered was not correctly formated!!', regex='^[A-Z]{3}/[A-Z]{3}/\\d{2}/\\d{5}$')]),
        ),
    ]
