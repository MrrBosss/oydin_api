# Generated by Django 4.0.10 on 2024-07-12 11:45

from django.db import migrations, models
import django.db.models.deletion
import oydin.models


class Migration(migrations.Migration):

    dependencies = [
        ('oydin', '0004_product_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('brand_image', models.ImageField(blank=True, upload_to=oydin.models.upload_to)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='oydin.brand')),
            ],
        ),
        migrations.CreateModel(
            name='ProductShots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_shots/')),
            ],
        ),
        migrations.DeleteModel(
            name='Characteristics',
        ),
        migrations.RemoveField(
            model_name='product',
            name='brand_image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product',
        ),
        migrations.AddField(
            model_name='productshots',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_shots', to='oydin.product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='oydin.brand'),
        ),
    ]
