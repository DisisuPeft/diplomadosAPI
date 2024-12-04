from django.shortcuts import render
from rest_framework.views import APIView
from myapps.authentication.permissions import HasRoleWithRoles
from myapps.authentication.models import UserCustomize
from myapps.authentication.serializers import UserCustomizeSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, status

class UsuariosAdministrador(APIView):
    permission_classes = [HasRoleWithRoles(["Administrador"]),  IsAuthenticated]
    def get(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return Response(
                {"error": "El usuario no se encuentra autenticado"}, 
                status=status.HTTP_401_UNAUTHORIZED
            )
    
        usuarios = UserCustomize.objects.exclude(email=user.email)
    
        if not usuarios.exists():
            return Response(
                {"error": "No se encontraron otros usuarios"}, 
                status=status.HTTP_404_NOT_FOUND
            )
    
        serializer = UserCustomizeSerializer(usuarios, many=True)
        return Response({"users": serializer.data}, status=status.HTTP_200_OK)  
