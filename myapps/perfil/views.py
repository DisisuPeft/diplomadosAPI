from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from myapps.authentication.decorators import role_required
from myapps.authentication.permissions import HasRoleWithRoles
from myapps.authentication.models import UserCustomize
from myapps.authentication.serializers import UserCustomizeSerializer

class ProfileOpt(APIView):
    permission_classes = [HasRoleWithRoles(['Administrador', 'Docente', 'Estudiante']), IsAuthenticated]
    def get(self, request):
        user_id = request.GET.get('id')
        user = UserCustomize.objects.get(id=user_id)
        if not user:
            return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserCustomizeSerializer(user)
        # serializer.data.pop('roleID', [])
        return Response({"profile": serializer.data}, status=status.HTTP_200_OK)