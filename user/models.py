from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    image = models.ImageField(default='default.png',
                              upload_to='profile_pics', blank=True)
    phone = models.CharField(max_length=11, default='-', blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)

    def __str__(self) -> str:
        return f'{self.user.username} Profile'


class Address(models.Model):
    city = models.CharField(max_length=50, default='-', blank=True)
    state = models.CharField(max_length=50, default='-', blank=True)
    country = models.CharField(max_length=50, default='-', blank=True)
    house_no = models.CharField(max_length=1000, default='-', blank=True)
    profile = models.OneToOneField(
        Profile, on_delete=models.CASCADE, related_name='address', blank=True)

    def __str__(self) -> str:
        return f'{self.profile.user.username} Address'
