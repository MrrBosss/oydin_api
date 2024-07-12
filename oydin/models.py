from django.db import models

# Create your models here.

def upload_to(instance, images):
    # Define the upload path
    return f'{instance.created_at.strftime("%Y/%m/%d")}/{images}'


class Product(models.Model):
    product = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to=upload_to, blank=True)
    brand_image = models.ImageField(upload_to=upload_to, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)



class Characteristics(models.Model):
    pass
