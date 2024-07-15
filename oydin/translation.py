from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register
from .models import Product, Category


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name','description','characteristic1','characteristic1value','characteristic2','characteristic2value',\
              'characteristic3','characteristic3value','extra_field_label','extra_field_value','dop_field_label','dop_field_value')

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)