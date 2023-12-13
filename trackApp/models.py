from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=255)
    date_of_purchase = models.DateField()
    # total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    item = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    def calculate_total_amount(self):
        return self.quantity * self.price

    def __str__(self):
        return f"{self.store_name} - {self.date_of_purchase}"
