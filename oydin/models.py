from django.db import models
from datetime import datetime

# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=100, null=True)
    brand_image = models.ImageField(upload_to='brand-images', blank=True)
   
    def __str__(self):
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length=100, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name



def upload_to(instance, filename):
    # Generate filename here
    if instance.created_at:
        date_str = instance.created_at.strftime("%Y/%m/%d")
    else:
        date_str = datetime.now().strftime("%Y/%m/%d")  # Or use any default date

    return f'{date_str}/{filename}'



class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to=upload_to, blank=True) 
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True) 
    description = models.CharField(max_length=500, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    characteristic1 = models.CharField(max_length=50,verbose_name='1.Xarakteristika nomi', null=True)
    characteristic1value = models.CharField(max_length=50,verbose_name='1.Xarakteristika qiymati', null=True)
    characteristic2 = models.CharField(max_length=50,verbose_name='2.Xarakteristika nomi', null=True)
    characteristic2value = models.CharField(max_length=50,verbose_name='2.Xarakteristika qiymati', null=True)
    characteristic3 = models.CharField(max_length=50,verbose_name='3.Xarakteristika nomi', null=True)
    characteristic3value = models.CharField(max_length=50,verbose_name='3.Xarakteristika qiymati', null=True)
    extra_field_label = models.CharField(max_length=50, verbose_name="1.Qo'shimcha xarakteristika nomi", null=True, blank=True)
    extra_field_value = models.CharField(max_length=50, verbose_name="1.Qo'shimcha xarakteristika qiymati", null=True, blank=True)
    dop_field_label = models.CharField(max_length=50, verbose_name="2.Qo'shimcha xarakteristika nomi", null=True, blank=True)
    dop_field_value = models.CharField(max_length=50, verbose_name="2.Qo'shimcha xarakteristika qiymati", null=True, blank=True)
   
    def __str__(self):
        
        return self.name


class ProductShots(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_shots')
    image = models.ImageField(upload_to=upload_to, blank=True) 
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"Shot for {self.product.name}"