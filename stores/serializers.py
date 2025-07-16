from rest_framework import serializers
from .models import Building, Floor, Category, Store, Amenity

class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'

class FloorSerializer(serializers.ModelSerializer):
    building = BuildingSerializer(read_only=True)

    class Meta:
        model = Floor
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class StoreSerializer(serializers.ModelSerializer):
    floor = FloorSerializer(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Store
        fields = '__all__'

class AmenitySerializer(serializers.ModelSerializer):
    store = StoreSerializer(read_only=True)

    class Meta:
        model = Amenity
        fields = '__all__'
