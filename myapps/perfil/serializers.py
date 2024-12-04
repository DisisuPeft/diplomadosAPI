from rest_framework import serializers
from myapps.perfil.models import Profile
# from myapps.authentication.serializers import UserCustomizeSerializer

class ProfileSerializer(serializers.ModelSerializer):
    # user = serializers.IntegerField(write_only=True, required=False)
    class Meta:
        model = Profile
        fields = ["nombre", "apellidoP", "apellidoM", "edad", "fechaNacimiento", "genero", "nivEdu", "telefono", "user"]

        def create(self, validated_data):
            profile = Profile.objects.create(
                nombre=validated_data['nombre'],
                apellidoP=validated_data['apellidoP'],
                apellidoM=validated_data['apellidoM'],
                edad=validated_data['edad'],
                fechaNacimiento=validated_data['fechaNacimiento'],
                genero=validated_data['genero'],
                nivEdu=validated_data['nivEdu'],
                telefono=validated_data['telefono'],
                userID=validated_data['userID']
            )
            profile.save()
            return profile

        def update(self, instance, validated_data):
            instance.userID = validated_data['userID']
            instance.save()
            return instance