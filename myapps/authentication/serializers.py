from myapps.authentication.models import UserCustomize, Roles, Permissions
from rest_framework import serializers

from myapps.perfil.models import Profile
from myapps.perfil.serializers import ProfileSerializer


class UserCustomizeSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = UserCustomize
        fields = ["id", "email", "password", "profile"]

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
        user = UserCustomize.objects.create_user(**validated_data)
        return user
    def update(self, instance, validated_data):
        instance.perfil_id = validated_data['id']

    def validate_email(self, value):
        if UserCustomize.objects.filter(email=value).exists():
            raise serializers.ValidationError("El email ya se encuentra registrado")
        return value



class RoleCustomizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = '__all__'

        def create(self, validated_data):
            role = Roles.objects.create(
                name=validated_data['name'],
            )
            role.save()
            return role


class PermissionCustomizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permissions
        fields = '__all__'
        def create(self, validated_data):
            permission = Permissions.objects.create(
                name=validated_data['name'],
                role=validated_data['role'],
            )
            permission.save()
            return permission