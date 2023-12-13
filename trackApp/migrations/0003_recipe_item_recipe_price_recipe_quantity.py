# Generated by Django 5.0 on 2023-12-13 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackApp', '0002_remove_recipe_name_remove_recipe_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='item',
            field=models.CharField(default='tomato', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]