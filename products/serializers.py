from rest_framework import serializers
from .models import Product, ProductCategory
from stores.serializers import StoreSerializer  # Optional: If you want nested store info

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    # Optional nested serializer
    store = StoreSerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
