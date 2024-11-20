from django.shortcuts import render
from contextvars import Token

from myapps.authentication.manager import CustomUserManager
from myapps.authentication.models import UserCustomize as User
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from myapps.authentication.serializers import UserCustomizeSerializer
from rest_framework import generics, status
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from myapps.perfil.serializers import ProfileSerializer
from myapps.perfil.models import Profile
# Create your views here.


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    if request.data['password'] != request.data['password_confirmation']:
        return Response({"error": "Las contraseñas no coinciden"}, status=status.HTTP_400_BAD_REQUEST)

    user_serializer = UserCustomizeSerializer(
        data={'email': request.data['email'], 'password': request.data['password'], 'role': request.data['role']}
    )
    #
    if user_serializer.is_valid():
        # print("we here")
        user = user_serializer.save()
        profile_data = {
            'nombre': request.data['nombre'],
            'apellidoP': request.data['apellidoP'],
            'user': user.id,
        }
        profile_serializer = ProfileSerializer(data=profile_data)
        if profile_serializer.is_valid():
            profile_serializer.save()
            return Response({"message": "Usuario creado con exito. Inicia sesión para continuar"}, status=status.HTTP_201_CREATED)
        else:
            return Response(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        # print(user_serializer.errors)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    email = request.data['email']
    password = request.data['password']

    if email is None or password is None:
        return Response({"message": "Por favor, proporciona un email y una contraseña."},
                        status=status.HTTP_400_BAD_REQUEST)
    if not User.objects.filter(email=email).exists():
        return Response({"message": "Usuario no encontrado."},
                        status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.get(email=email)

    if not user.check_password(request.data['password']):
        return Response({"message": "La contraseña es incorrecta."},
                        status=status.HTTP_400_BAD_REQUEST)

    token = RefreshToken.for_user(user)
    s = UserCustomizeSerializer(user)

    return Response({'token': str(token.access_token), 'refreshToken': str(token), 'user': s.data}, status=status.HTTP_200_OK)


# def user(request):
