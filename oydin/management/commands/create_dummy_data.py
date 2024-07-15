from django.core.management.base import BaseCommand
from django.utils import timezone
import requests
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from oydin.models import Product, ProductShots, Category, Brand
from faker import Faker
import random 

fake = Faker()
fake_ru = Faker('ru_RU')
fake_uz = Faker('tr_TR')

class Command(BaseCommand):
    help = 'Creates 50 records for Product, ProductShots, Category, and Brand models using Faker'

    def handle(self, *args, **kwargs):
        categories = self.create_categories()
        brands = self.create_brands()

        for _ in range(50):
            category = random.choice(categories)
            brand = random.choice(brands)
            image_url= self.get_product_shot_image()
            image_name = f"product_{fake.word()}.jpg"  # Generate a unique image name
            image_path = self.save_image_from_url(image_url, image_name)
            product = Product.objects.create(
                name_en=fake.word(),
                name_ru=fake_ru.word(),
                name=fake_uz.word(),
                description_ru=fake_ru.text(),
                description_en=fake.text(),
                description=fake_uz.text(),
                category=category,
                brand=brand,
                image=image_path,
                characteristic1=fake.word(),
                characteristic2=fake.word(),
                characteristic3=fake.word(),
                extra_field_label=fake.word(),
                extra_field_value=fake.word(),
                dop_field_label=fake.word(),
                dop_field_value=fake.word(),
            )

            for shot_num in range(1, 3):  # Create 5 ProductShots for each Product
                image_url = self.get_product_shot_image()
                if image_url:
                    image_name = f"product_{_ + 1}_shot_{shot_num}.jpg"  # Generate a unique image name
                    image_path = self.save_image_from_url(image_url, image_name)
                    if image_path:
                        ProductShots.objects.create(
                            product=product,
                            image=image_path,
                            created_at=timezone.now(),
                        )

            self.stdout.write(self.style.SUCCESS(f'Successfully created Product {_ + 1} and its shots.'))

        self.stdout.write(self.style.SUCCESS('Successfully created 50 products with shots.'))

    def create_categories(self):
        categories = []
        for _ in range(1, 11):  # Create 10 categories
            category, created = Category.objects.get_or_create(
                name=fake_uz.word(), defaults={'name_ru':fake_ru.word(), 'name_en':fake.word()}
            )
            categories.append(category)
        return categories

    def create_brands(self):
        brands = []
        for _ in range(1, 6):  # Create 5 brands
            brand, created = Brand.objects.get_or_create(
                name=fake.company()
            )
            brands.append(brand)
        return brands


    def get_product_shot_image(self):
        # Example using Unsplash API to fetch random product shot image
        access_key = ''  # Replace with your Unsplash access key
        url = f'https://api.unsplash.com/photos/random?query=product&orientation=landscape'
        headers = {
            'Accept-Version': 'v1',
            'Authorization': f'Client-ID {access_key}'
        }
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            return data['urls']['regular']  # Get regular size image URL
        else:
            print(response.text)
            return ''  # Handle error case, e.g., return a default image URL
    def save_image_from_url(self, url, image_name):
        # Download image from URL and save it using default storage
        try:
            response = requests.get(url)
            if response.status_code == 200:
                # Generate a unique file name
                image_path = f'product_shots/{image_name}'  # Adjust path as needed
                # Save image to default storage (filesystem)
                default_storage.save(image_path, ContentFile(response.content))
                return image_path
            else:
                return None
        except Exception as e:
            self.stderr.write(f'Failed to save image from URL: {str(e)}')
            return None