from django.db import models

# Create your models here.
class Product(models.Model):
    ProductName = models.CharField(max_length=100)

class Item(models.Model):
    ItemName = models.CharField(max_length=100)
    ItemQuantity = models.IntegerField()
    ItemDescription = models.CharField(max_length=500)
    PhotoFileName = models.ImageField('ItemImage')
    Product = models.ForeignKey( Product, on_delete = models.CASCADE, related_name='productItem')