from django.db import models
from datetime import datetime

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



class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to=upload_to, blank=True) 
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True) 
    description = models.CharField(max_length=500, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    characteristic_n1= models.CharField(max_length=50,verbose_name='1.Xarakteristika nomi', null=True, blank=True)
    characteristic_v1 = models.CharField(max_length=50,verbose_name='1.Xarakteristika qiymati', null=True, blank=True)
    characteristic_n2= models.CharField(max_length=50,verbose_name='2.Xarakteristika nomi', null=True, blank=True)
    characteristic_v2= models.CharField(max_length=50,verbose_name='2.Xarakteristika qiymati', null=True, blank=True)
    characteristic_n3= models.CharField(max_length=50,verbose_name='3.Xarakteristika nomi', null=True, blank=True)
    characteristic_v3= models.CharField(max_length=50,verbose_name='3.Xarakteristika qiymati', null=True, blank=True)
    extra_field_label = models.CharField(max_length=50, verbose_name="1.Qo'shimcha xarakteristika nomi", null=True, blank=True)
    extra_field_value = models.CharField(max_length=50, verbose_name="1.Qo'shimcha xarakteristika qiymati", null=True, blank=True)
    dop_field_label = models.CharField(max_length=50, verbose_name="2.Qo'shimcha xarakteristika nomi", null=True, blank=True)
    dop_field_value = models.CharField(max_length=50, verbose_name="2.Qo'shimcha xarakteristika qiymati", null=True, blank=True)
   
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