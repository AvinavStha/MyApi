from .models import Item,Product  
from rest_framework import serializers

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'ItemName', 'ItemQuantity', 'ItemDescription', 'PhotoFileName']

class ProductSerializer(serializers.ModelSerializer):
    productItem = ItemSerializer(many = True, read_only =True)
    class Meta:
        model = Product
        fields = ['id', 'ProductName', 'productItem']