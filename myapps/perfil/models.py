from django.db import models
from django.db.models import OneToOneField
from django.db.models.fields.related import ForeignKey
# Create your models here.
class Profile(models.Model):
    nombre = models.CharField(max_length=100)
    apellidoP = models.CharField(max_length=100)
    apellidoM = models.CharField(max_length=100, null=True)
    edad = models.IntegerField(null=True)
    fechaNacimiento = models.DateField(null=True)
    genero = models.CharField(max_length=100, null=True)
    nivEdu = models.IntegerField(null=True)
    telefono = models.CharField(max_length=15, null=True)
    user = OneToOneField('authentication.UserCustomize', on_delete=models.SET_NULL, related_name='profile', null=True)