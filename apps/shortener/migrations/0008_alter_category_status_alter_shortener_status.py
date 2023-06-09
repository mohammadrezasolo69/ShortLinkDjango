# Generated by Django 4.1.7 on 2023-03-28 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0007_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.CharField(choices=[('AC', 'Active'), ('IA', 'Inactive')], default='AC', max_length=2, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='shortener',
            name='status',
            field=models.CharField(choices=[('AC', 'Active'), ('IA', 'Inactive')], default='AC', max_length=2, verbose_name='Status'),
        ),
    ]
