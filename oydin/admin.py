from django.contrib import admin
from .models import Product, Brand, Category,  Characteristic, ProductShots
from modeltranslation.admin import TabbedTranslationAdmin, TranslationTabularInline
# Register your models here.

class ProductShotsInline(admin.TabularInline):
    model = ProductShots
    extra = 0

class CharacteristicInline(TranslationTabularInline):
    model = Characteristic
    extra = 1  # Number of extra inline forms to display

@admin.register(Product)
class ProductAdmin(TabbedTranslationAdmin):
    list_display = ['name_uz','brand','id']
    search_fields = ['name_uz']
    # group_fieldsets = True
    inlines = [CharacteristicInline, ProductShotsInline]

@admin.register(Category)
class CategoryAdmin(TabbedTranslationAdmin):
    list_display = ['name_uz','id']
    search_fields = ['name_uz']

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name','id']
    search_fields = ['name']
