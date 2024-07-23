import django_filters
from .models import Product, Brand, Category



class ProductFilter(django_filters.FilterSet):
    # Define filters for brand name and category
    brand = django_filters.ModelMultipleChoiceFilter(field_name='brand', queryset=Brand.objects.all())
    category = django_filters.ModelMultipleChoiceFilter(field_name='category', queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = ['brand', 'category']
