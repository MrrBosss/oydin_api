from rest_framework import serializers
from .models import Product, Brand, ProductShots, Category, Characteristic, Order, OrderItem


class ProductShotsSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = ProductShots
        fields = '__all__'


class CharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characteristic
        fields = ['id','product','name','value']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name_uz", "name_ru", "name_en", "image", "category", "created_at", "brand"]


class ProductDetailSerializer(serializers.ModelSerializer):
    product_shots = ProductShotsSerilaizer(many=True)
    characteristics = CharacteristicSerializer(many=True)
    class Meta:
        model = Product
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'product']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'order_date', 'name', 'phone_number', 'email','message','items']

    def validate_items(self, value):
        if not value:
            raise serializers.ValidationError("Items list cannot be empty")
        return value

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order
