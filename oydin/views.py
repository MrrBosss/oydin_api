from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Product
from .serializers import ProductSerializer
# Create your views here.



class ProductViewSet(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # http_method_names = ['get']