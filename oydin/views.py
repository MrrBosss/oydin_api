from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .models import Product, Brand, ProductShots, Category
from .serializers import ProductSerializer, BrandSerializer, ProductShotsSerilaizer, CategorySerializer
from .filters import ProductFilter
# Create your views here.

from rest_framework import filters

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    http_method_names = ['get']



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get']
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get'] 
    pagination_class = None


class ProductShotsViewSet(viewsets.ModelViewSet):
    queryset = ProductShots.objects.all()
    serializer_class = ProductShotsSerilaizer
    http_method_names = ['get'] 
    pagination_class = None


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    http_method_names = ['get'] 
    pagination_class = None