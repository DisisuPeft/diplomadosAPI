from myapps.authentication.models import UserCustomize, Roles, Permissions
from rest_framework import serializers
from myapps.perfil.models import Profile
from myapps.perfil.serializers import ProfileSerializer
from django.db import transaction
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from rest_framework import exceptions




