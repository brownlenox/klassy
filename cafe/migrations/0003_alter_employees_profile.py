# Generated by Django 4.2.7 on 2023-11-13 16:05

import cafe.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0002_employees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='profile',
            field=models.ImageField(blank=True, null=True, upload_to=cafe.models.unique_image_name),
        ),
    ]
