from django.contrib import admin
from .models import Product, Brand, Category,  Characteristic, ProductShots, Order, OrderItem, News
from modeltranslation.admin import TabbedTranslationAdmin, TranslationTabularInline
from django.utils.safestring import mark_safe


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_date', 'id']
    list_display_links =  ['order_date','id']
    inlines = [OrderItemInline]

    def get_total_quantity(self, obj):
        return sum(item.quantity for item in obj.items.all())

    get_total_quantity.short_description = 'Total Quantity'


class ProductShotsInline(admin.TabularInline):
    model = ProductShots
    extra = 0

class CharacteristicInline(TranslationTabularInline):
    model = Characteristic
    extra = 1  # Number of extra inline forms to display

@admin.register(Product)
class ProductAdmin(TabbedTranslationAdmin):
    list_display = ['name_uz', 'photo', 'brand','id']
    search_fields = ['name_uz']
    list_display_links =  ['name_uz', 'photo']
    # group_fieldsets = True
    inlines = [CharacteristicInline, ProductShotsInline]

    def photo(self, obj):
        image = obj.image.url if obj.image else ""
        return mark_safe(
            f'<img src="{image}" width="200"/>'  # if obj.logo_light else '<div>Rasmsiz</div>'
        )

    photo.short_description = 'Логотип'
    photo.allow_tags = True


@admin.register(Category)
class CategoryAdmin(TabbedTranslationAdmin):
    list_display = ['name_uz','id']
    search_fields = ['name_uz']

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name','id']
    search_fields = ['name']

@admin.register(News)
class NewsAdmin(TabbedTranslationAdmin):
    list_display = ['name_uz']
    search_fields = ["name_uz"]