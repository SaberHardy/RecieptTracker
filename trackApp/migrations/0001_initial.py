# Generated by Django 5.0 on 2023-12-12 02:04

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_of_purchase', models.DateTimeField(default=django.utils.timezone.now)),
                ('price', models.DecimalField(decimal_places=2, max_digits=1000)),
            ],
        ),
    ]
