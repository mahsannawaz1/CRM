from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from .models import Profile, Address
from django.dispatch import receiver


@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def saveProfile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(post_save, sender=Profile)
def createAddress(sender, instance, created, **kwargs):
    if created:
        Address.objects.create(profile=instance)


@receiver(post_save, sender=Profile)
def saveAddress(sender, instance, **kwargs):
    instance.address.save()


@receiver(post_save, sender=User)
def addGroup(sender, instance, created, **kwargs):
    if created:
        if instance.is_superuser:
            admin = Group.objects.get(name='admin')
            instance.groups.add(admin)
            instance.save()

        customer_group = Group.objects.get(name='customer')
        instance.groups.add(customer_group)
        instance.save()
