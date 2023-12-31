# Generated by Django 4.2.7 on 2023-11-13 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('guests_number', models.IntegerField()),
                ('date', models.DateField()),
                ('time', models.CharField(max_length=20)),
                ('message', models.TextField()),
            ],
        ),
    ]
