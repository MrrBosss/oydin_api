from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .models import Product, Brand, ProductShots, Category, Characteristic, Order, News
from .serializers import ProductSerializer, BrandSerializer, ProductShotsSerilaizer, CategorySerializer, \
     ProductDetailSerializer, CharacteristicSerializer, OrderSerializer, NewsSerializer
from .filters import ProductFilter
# Create your views here.


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name_uz', 'name_ru', 'name_en']
    filterset_class = ProductFilter


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get'] 
    pagination_class = None


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
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


class CharacteristicViewSet(viewsets.ModelViewSet):
    queryset = Characteristic.objects.all()
    serializer_class = CharacteristicSerializer
    http_method_names = ['get']
    pagination_class = None


class OrderView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    http_method_names = ['post']