from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register
from .models import Product, Category


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)