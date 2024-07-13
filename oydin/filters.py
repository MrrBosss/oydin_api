import django_filters
from .models import Product, Brand



class ProductFilter(django_filters.FilterSet):
    # Define filters for brand name and category
    brand__name = django_filters.CharFilter(field_name='brand__name', lookup_expr='icontains')
    category__name = django_filters.CharFilter(field_name='category__name', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['brand__name', 'category__name']
