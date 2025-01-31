from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db.models.fields.related import ForeignKey

from myapps.authentication.manager import CustomUserManager
from myapps.perfil.models import Profile

class Roles(models.Model):
    name = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return self.name

class UserCustomize(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    # perfil = models.OneToOneField(Profile, on_delete=models.SET_NULL, related_name='user_customize', null=True)
    roleID = models.ManyToManyField(Roles, related_name='user_customize')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    # groups = models.ManyToManyField(
    #     Group,
    #     related_name='usercustomize_set',
    #     blank=True,
    #     help_text='The groups this user belongs to.',
    #     verbose_name='groups'
    # )
    # user_permissions = models.ManyToManyField(
    #     Permission,
    #     related_name='usercustomize_set',
    #     blank=True,
    #     help_text='Specific permissions for this user.',
    #     verbose_name='user permissions'
    # )
# Create your models here.

    def __str__(self):
        return self.email



class Permissions(models.Model):
    name = models.CharField(max_length=10, unique=True)
    role = models.ManyToManyField(Roles, related_name='permission')