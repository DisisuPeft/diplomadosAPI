from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from myapps.authentication.decorators import role_required
# Create your views here.

# @api_view(["GET"])
# @role_required(["Admin"])
# @permission_classes([IsAuthenticated])
# def getprofile(request):
#     return Response("Hola y bienvenido a la primera ruta protegida", status=status.HTTP_200_OK)