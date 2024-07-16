from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register
from .models import Product, Category, Characteristic


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name','description')

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Characteristic)
class CharacteristicTranslationOptions(TranslationOptions):
    fields = ('name','value')