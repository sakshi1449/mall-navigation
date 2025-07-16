from django.contrib import admin
from .models import Building, Floor, Category, Store, Amenity

@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    search_fields = ('name', 'address')

@admin.register(Floor)
class FloorAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'building')
    list_filter = ('building',)
    search_fields = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'description')

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'floor', 'category')
    list_filter = ('floor', 'category')
    search_fields = ('name', 'description')

@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ('type', 'store')
    list_filter = ('type',)
    search_fields = ('type', 'description')
