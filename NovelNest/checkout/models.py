from django.db import models

class Order(models.Model):
    book_name = models.CharField(max_length=100, default='The Alchemist')
    book_price = models.DecimalField(max_digits=10, decimal_places=2, default=299)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=1)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    cod = models.BooleanField(default=True)
    order_id = models.AutoField(primary_key=True)
