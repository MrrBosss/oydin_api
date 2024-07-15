from django.contrib import admin
from .models import Product, Brand, Category, ProductShots
from modeltranslation.admin import TabbedTranslationAdmin
# Register your models here.

class ProductShotsInline(admin.TabularInline):
    model = ProductShots
    extra = 0

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name','id']
    search_fields = ['name']

@admin.register(Product)
class ProductAdmin(TabbedTranslationAdmin):
    list_display = ['name_uz','brand','id']
    search_fields = ['name_uz']
    # group_fieldsets = True
    inlines = [ProductShotsInline]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name_uz','id']
    search_fields = ['name_uz']

# admin.site.register(ProductShots)