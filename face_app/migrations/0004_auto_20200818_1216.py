# Generated by Django 3.0.8 on 2020-08-18 09:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face_app', '0003_auto_20200817_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phoneNumber',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Phone number entered was not correctly formated!!', regex='^\\+?1?\\d{10,13}$')]),
        ),
        migrations.AlterField(
            model_name='student',
            name='regno',
            field=models.CharField(max_length=30, unique=True, validators=[django.core.validators.RegexValidator(message='Registration Number entered was not correctly formated!!', regex='[A-Z]{3}/[A-Z]{3}/\\d{2}/?\\d{5}')]),
        ),
    ]