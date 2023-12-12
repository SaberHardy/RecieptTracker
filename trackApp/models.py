from django.db import models
from django.utils import timezone


class ItemModel(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False, default=1)
    price = models.FloatField(null=False, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.name


class Recipe(models.Model):
    item = models.ForeignKey(ItemModel, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    date_of_purchase = models.DateTimeField(default=timezone.now)
    price = models.DecimalField(max_digits=1000, decimal_places=2)

    def calculate_total_amount(self):
        # Calculate the total amount based on the prices of items
        total_amount = self.item.price * self.item.quantity
        return total_amount

    def __str__(self):
        return self.name
