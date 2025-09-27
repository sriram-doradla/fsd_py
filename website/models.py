# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# class Product(models.Model):
#     productname = models.CharField(max_length=250)
#     description = models.TextField(null=True, blank=True)
#     price = models.FloatField()

#     def __str__(self):
#         return self.productname
    
# # if we dont have name also by defAuth
# @receiver(post_save, sender = 'website.AuthUser')
# def create_auth_user_token(sender,instance, created,**kwargs):
#     if created:
#         from rest_framework.authtoken.models import Token
#         Token.objects.create(user=instance)
# class AuthUser(AbstractUser):
#     email = models.EmailField(unique=True)
#     username = models.CharField(max_length=150, unique=True)
#     # REQUIRED_FIELDS = ['email', 'username']
#     user_permissions = None
#     groups = None
#     first_name = None
#     last_name = None

#     def __str__(self):
#         return self.email


from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Product(models.Model):
    productname = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()

    def __str__(self):
        return self.productname


class AuthUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)

    # remove unused fields safely
    first_name = None
    last_name = None
    user_permissions = None
    groups = None

    def __str__(self):
        return self.email


@receiver(post_save, sender=AuthUser)
def create_auth_user_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)
