from myapps.authentication.models import UserCustomize, Roles, Permissions
from rest_framework import serializers
from myapps.perfil.models import Profile
from myapps.perfil.serializers import ProfileSerializer
from django.db import transaction

class RoleCustomizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = ["id", "name"]

        def create(self, validated_data):
            role = Roles.objects.create(
                name=validated_data['name'],
            )
            role.save()
            return role


class PermissionCustomizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permissions
        fields = ["id", "name"]
        def create(self, validated_data):
            permission = Permissions.objects.create(
                name=validated_data['name'],
            )
            permission.save()
            return permission

class UserCustomizeSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=False)
    role = serializers.IntegerField(write_only=True, required=False)
    class Meta:
        model = UserCustomize
        fields = ["id", "email", "password", "profile", "role"]

    email = serializers.CharField(
        required=True,
        error_messages={
            'blank': "El email del usuario no puede estar vacío.",
            'required': "El email del usuario es obligatorio."
        }
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        error_messages={
            'blank': "El campo contraseña no puede estar vacío.",
            'required': "La contraseña es obligatoria."
        }
    )


    def create(self, validated_data):
        role_id = validated_data.pop('role', None)
        print(role_id)
        try:
            with transaction.atomic():

                user = UserCustomize.objects.create_user(
                    email=validated_data['email'],
                    password=validated_data['password'],
                )
                if role_id is not None:
                    try:
                        role = Roles.objects.get(id=role_id)
                        user.roleID.add(role)
                    except Roles.DoesNotExist:
                        raise serializers.ValidationError("El rol especificado no existe")
                return user
        except Exception as e:
            raise serializers.ValidationError(str(e))

    # def update(self, instance, validated_data):
        # instance.perfil_id = validated_data['id']

    def validate_email(self, value):
        if UserCustomize.objects.filter(email=value).exists():
            raise serializers.ValidationError("El email ya se encuentra registrado")
        return value


