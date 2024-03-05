from django.db import models

class landing_seller(models.Model):
    SELLER_ID = models.IntegerField(primary_key=True)
    SELLER_NAME = models.CharField(max_length=20)

class landing_book(models.Model):
    B_ID = models.IntegerField(primary_key=True)
    BNAME = models.CharField(max_length=30)
    SELLER_ID_id = models.ForeignKey(landing_seller, on_delete=models.CASCADE)
    PRICE = models.IntegerField()
    COVER_PAGE = models.BinaryField()
    IMAGE = models.CharField(max_length=30, default='Alchemist.jpg')