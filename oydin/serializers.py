from rest_framework import serializers
from .models import Product, Brand, ProductShots, Category



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ProductShotsSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = ProductShots
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


