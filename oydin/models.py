from django.db import models

# Create your models here.


class Product(models.Model):
    product = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='images', blank=True)
    brand_image = models.ImageField(upload_to='brand_images', blank=True)



