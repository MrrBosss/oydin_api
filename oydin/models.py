from django.db import models
from datetime import datetime

from .validators import validate_name, validate_phone_number
# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=100, null=True)
    brand_image = models.ImageField(upload_to='brand-images', blank=True)
   
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Brend"
        verbose_name_plural = "Brendlar"


class Category(models.Model):
    name = models.CharField(max_length=100, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name_uz

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"


def upload_to(instance, filename):
    # Generate filename here
    if instance.created_at:
        date_str = instance.created_at.strftime("%Y/%m/%d")
    else:
        date_str = datetime.now().strftime("%Y/%m/%d")  # Or use any default date

    return f'{date_str}/{filename}'


class Characteristic(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='characteristics')
    name = models.CharField(max_length=50, verbose_name='Xarakteristika nomi',null=True,blank=True)
    value = models.CharField(max_length=50, verbose_name='Xarakteristika qiymati',null=True,blank=True)
    name = models.CharField(max_length=50, verbose_name='Xarakteristika nomi',null=True,blank=True)
    value = models.CharField(max_length=50, verbose_name='Xarakteristika qiymati',null=True,blank=True)

    def __str__(self):
        return f"{self.name}: {self.value}"
    
    class Meta:
        verbose_name = 'Xarakteristika'
        verbose_name_plural = 'Xarakteristikalar'


class Product(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True )
    image = models.ImageField(upload_to=upload_to, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=500, null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name_uz
    
    class Meta:
        verbose_name = "Maxsulot"
        verbose_name_plural = "Maxsulotlar"


class ProductShots(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_shots')
    image = models.ImageField(upload_to=upload_to) 
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"Shot for {self.product.name}"
    
    class Meta:
        verbose_name = "Maxsulot rasmi"
        verbose_name_plural = "Maxsulot rasmlari"


class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True, null=True)
    name = models.CharField(max_length=100, null=True, validators=[validate_name])
    phone_number = models.CharField(max_length=20, null=True, validators=[validate_phone_number])
    email = models.EmailField(null=True,blank=True)
    message = models.TextField(null=True,blank=True)
    # Add other fields like customer information, shipping details, etc.

    class Meta:
        verbose_name = "Buyurtma"
        verbose_name_plural = "Buyurtmalar"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product.name)

    class Meta:
        verbose_name = "Buyurtma"
        verbose_name_plural = "Buyurtmalar"
        

class News(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to=upload_to, blank=True)
    description = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.name_uz
    
    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"
        