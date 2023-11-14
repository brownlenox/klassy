# Generated by Django 4.2.7 on 2023-11-13 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=30)),
                ('social_fb', models.CharField(max_length=100)),
                ('social_tweet', models.CharField(max_length=100)),
                ('social_ig', models.CharField(max_length=100)),
                ('profile', models.ImageField(blank=True, upload_to='')),
            ],
        ),
    ]
