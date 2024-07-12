from django.contrib import admin
from .models import Product, Brand, Category, ProductShots
# Register your models here.

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name','id']
    search_fields = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','brand','id']
    search_fields = ['name']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','id']
    search_fields = ['name']

admin.site.register(ProductShots)