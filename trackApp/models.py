from django.db import models
from django.utils import timezone


class ItemModel(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False, default=1)
    price = models.FloatField(null=False, blank=False)
    description = models.TextField()

    def get_total_item_price(self):
        return self.quantity * self.price

    def __str__(self):
        return self.name


class Recipe(models.Model):
    items = models.ManyToManyField(ItemModel)
    name = models.CharField(max_length=100, null=False, blank=False)
    date_of_purchase = models.DateTimeField(default=timezone.now)
    price = models.DecimalField(max_digits=1000, decimal_places=2)

    def calculate_total_amount(self):
        total_amount = 0
        for order_item in self.items.all():
            total_amount += order_item.get_total_item_price()
        return total_amount

    def __str__(self):
        return self.name
