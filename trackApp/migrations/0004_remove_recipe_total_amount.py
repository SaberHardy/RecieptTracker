# Generated by Django 5.0 on 2023-12-13 00:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trackApp', '0003_recipe_item_recipe_price_recipe_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='total_amount',
        ),
    ]
