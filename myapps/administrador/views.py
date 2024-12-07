from django.shortcuts import render
from rest_framework.views import APIView
from myapps.authentication.permissions import HasRoleWithRoles
from myapps.authentication.models import UserCustomize
from myapps.authentication.serializers import UserCustomizeSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, status
from myapps.perfil.models import Profile
from myapps.perfil.serializers import ProfileSerializer

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
    
    def patch(self, request, *args, **kwargs):
        user_id = request.data['id']  
        
        try:
            user = UserCustomize.objects.get(id=user_id)
            profile = user.profile  # Asumo que tienes una relación de perfil
            # serializer = ProfileSerializer(profile)
            # return Response({"response": serializer.data}, status=status.HTTP_200_OK)
        except UserCustomize.DoesNotExist:
            return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        
        # # Preparar datos para actualización
        # user_data = {}
        profile_data = {}
        
        # # Campos de usuario
        if 'email' in request.data and request.data['email']:
            user.email = request.data['email']
        
        if 'password' in request.data and request.data['password']:
            user.set_password(request.data['password'])
        if 'role' in request.data and request.data['role']:
            role = request.data['role']
            separated = role.split(',')
            user.roleID.add(*separated)
        
        user.save()
        # if 'role' in request.data and request.data['role']:
        #     user.role = request.data['role']
        
        # # Campos de perfil
        perfil_campos = [
            "nombre", "apellidoP", "apellidoM", "edad", 
            "fechaNacimiento", "genero", "nivEdu", "telefono"
        ]
        
        for campo in perfil_campos:
            # print(campo)
            if campo in request.data and request.data[campo]:
                profile_data[campo] = request.data[campo]
                # if request.data[campo] == 'null':
                #     profile_data[campo] = request.data[campo]
        
        # # Serializers para actualización
        # user_serializer = UserCustomizeSerializer(
        #     user, 
        #     data=user_data, 
        #     partial=True  # Permite actualizaciones parciales
        # )
        profile_serializer = ProfileSerializer(
            profile, 
            data=profile_data, 
            partial=True  # Permite actualizaciones parciales
        )
        
        try:
        #     # Validar y guardar
            # if user_data:
            #     if user_serializer.is_valid():
            #         user_serializer.save()
            
            if profile_data:
                if profile_serializer.is_valid():
                    profile_serializer.save()
                else:
                    return Response({
                        "error": "Error al actualizar el perfil", 
                        "details": profile_serializer.errors
                    }, status=status.HTTP_400_BAD_REQUEST)
            
            return Response({"message": "Usuario editado"}, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                "error": "Error en la actualización", 
                "details": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

        # email = request.data['email']
        # password = request.data['password']
        # user_serializer = UserCustomizeSerializer(email=email, password=password)
        # if user_serializer.is_valid():
        #     user = user_serializer.save()
        #     perfil_dict = {
        #         "nombre": request.data["nombre"],
        #         "apellidoP": request.data["apellidoP"],
        #         "apellidoM": request.data["apellidoM"],
        #         "edad": request.data["edad"],
        #         "fechaNacimiento": request.data["fechaNacimiento"],
        #         "genero": request.data["genero"],
        #         "nivEdu": request.data["nivEdu"],
        #         "telefono": request.data["telefono"],
        #         "user": user.id
        #     }
        #     profile_serializer = ProfileSerializer(data=perfil_dict)
        #     if profile_serializer.is_valid():
        #         profile_serializer.save()
        #         return Response({"message":"Usuario editado"}, status=status.HTTP_200_OK)
        #     else:
        #         return Response({"error":"Error al actualizar el usuario"}, status=status.HTTP_400_BAD_REQUEST)

# class EditUsers(APIView):
#     permission_classes = [HasRoleWithRoles(["Administrador"]),  IsAuthenticated]
#     def patch(self, request, *args, **kwargs):
#         email = request.data['email']
#         password = request.data['password']
#         user_serializer = UserCustomizeSerializer(email=email, password=password)
#         if user_serializer.is_valid():
#             user = user_serializer.save()
#             perfil_dict = {
#                 "nombre": request.data["nombre"],
#                 "apellidoP": request.data["apellidoP"],
#                 "apellidoM": request.data["apellidoM"],
#                 "edad": request.data["edad"],
#                 "fechaNacimiento": request.data["fechaNacimiento"],
#                 "genero": request.data["genero"],
#                 "nivEdu": request.data["nivEdu"],
#                 "telefono": request.data["telefono"],
#                 "user": user.id
#             }
#             profile_serializer = ProfileSerializer(data=perfil_dict)
#             if profile_serializer.is_valid():
#                 profile_serializer.save()
#                 return Response({"message":"Usuario editado"}, status=status.HTTP_200_OK)
#             else:
#                 return Response({"error":"Error al actualizar el usuario"}, status=status.HTTP_400_BAD_REQUEST)
            
    # nombre: "",
    # apellidoP: "",
    # apellidoM: "",
    # edad: null,
    # fechaNacimiento: "",
    # genero: "",
    # nivEdu: "",
    # telefono: "",
    # email: "",
    # password: "",
    # role: null,
        # perfil_dict = {
        #     "nombre": request.data["nombre"],
        #     "apellidoP": request.data["apellidoP"],
        #     "apellidoM": request.data["apellidoM"],
        #     "edad": request.data["edad"],
        #     "fechaNacimiento": request.data["fechaNacimiento"],
        #     "genero": request.data["genero"],
        #     "nivEdu": request.data["nivEdu"],
        #     "telefono": request.data["telefono"],
        # }