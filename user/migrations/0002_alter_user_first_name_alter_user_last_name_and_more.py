# Generated by Django 5.0.3 on 2024-04-01 07:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(code='nomatch', message='Name must contain only letters and be at least 3 characters long', regex='^[a-zA-Z]{3,}$')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(code='nomatch', message='Name must contain only letters and be at least 3 characters long', regex='^[a-zA-Z]{3,}$')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(code='nomatch', message='', regex='^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@$!%*?&])[A-Za-z\\d@$!%*?&]{8,16}$')]),
        ),
    ]
