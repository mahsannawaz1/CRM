# Generated by Django 4.1.4 on 2023-04-20 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_remove_product_order_order_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='img_default.jpg', upload_to='product_pics'),
        ),
    ]
