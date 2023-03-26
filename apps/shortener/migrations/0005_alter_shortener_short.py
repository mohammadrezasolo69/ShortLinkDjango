# Generated by Django 4.1.7 on 2023-03-26 18:34

import apps.shortener.validator
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0004_alter_shortener_short'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortener',
            name='short',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True, validators=[apps.shortener.validator.NoAspacesAllowed], verbose_name='Short'),
        ),
    ]
