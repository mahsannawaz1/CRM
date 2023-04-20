from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    weight = models.DecimalField(decimal_places=2, max_digits=6)
    barcode = models.CharField(max_length=12)
    inventory = models.PositiveIntegerField()
    image = models.ImageField(
        default='img_default.jpg', upload_to='product_pics/', blank=True)

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    ORDER_CHOICES = [
        ('P', 'Pending'), ('D', 'Delievered'), ('C', 'Canceled')
    ]
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    order_status = models.CharField(
        max_length=1, choices=ORDER_CHOICES, default='P')
    customer = models.ForeignKey(User, on_delete=models.PROTECT)
    discount = models.DecimalField(max_digits=6, decimal_places=2)
    product = models.ManyToManyField(
        Product, related_name='order')

    def __str__(self) -> str:
        return f'{self.customer.username} Order'

    def get_absolute_url(self):
        return reverse('list_orders')
