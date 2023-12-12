from django.db import models
from django.utils import timezone


class Recipe(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    date_of_purchase = models.DateTimeField(default=timezone.now)
    price = models.DecimalField(max_digits=1000, decimal_places=2)

    def calculate_total_amount(self):
        # Retrieve all items related to the current recipe
        items = Recipe.objects.filter(name=self.name)

        # Calculate the total amount based on the prices of items
        total_amount = sum(item.price for item in items)

        return total_amount

    def __str__(self):
        return self.name

