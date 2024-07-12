import django_filters
from .models import Product, Brand


class ProductFilter(django_filters.FilterSet):
    brand = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Product
        fields = ['brand']