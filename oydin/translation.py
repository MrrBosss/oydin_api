from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register
from .models import Product, Category


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name','description','extra_field_label','extra_field_value','dop_field_label','dop_field_value',\
              'characteristic_n1','characteristic_n2','characteristic_n3')

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)