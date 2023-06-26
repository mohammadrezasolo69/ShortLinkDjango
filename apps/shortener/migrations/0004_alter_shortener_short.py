# Generated by Django 4.1.7 on 2023-03-26 18:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0003_shortener_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortener',
            name='short',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True, validators=[django.core.validators.RegexValidator(message='No spaces allowed', regex='^[^\\s]+$')], verbose_name='Short'),
        ),
    ]
