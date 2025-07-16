from django.contrib import admin
from .models import ProductCategory, Product

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'description')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'store', 'category', 'price', 'in_stock')
    list_filter = ('store', 'category', 'in_stock')
    search_fields = ('name', 'description')
