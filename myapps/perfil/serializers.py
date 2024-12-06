from rest_framework import serializers
from myapps.perfil.models import Profile
# from myapps.authentication.serializers import UserCustomizeSerializer

class ProfileSerializer(serializers.ModelSerializer):
    # user = serializers.IntegerField(write_only=True, required=False)
    class Meta:
        model = Profile
        fields = ["nombre", "apellidoP", "apellidoM", "edad", "fechaNacimiento", "genero", "nivEdu", "telefono", "user"]
        extra_kwargs = {field: {'required': False} for field in fields}
        # extra_kwargs = {
        #     'edad': {'required': False, 'allow_null': True},
        #     'fechaNacimiento': {'required': False, 'allow_null': True},
        #     'nivEdu': {'required': False, 'allow_null': True}
        # }

    # def to_internal_value(self, data):
    #     # Convertir cadenas vacías a None antes de validarlas
    #     for key, value in data.items():
    #         if value == '':
    #             data[key] = None
    #     print(data)
    #     return super().to_internal_value(data)

    # def validate(self, attrs):
    #     # Validaciones personalizadas adicionales (si necesitas)
    #     return attrs
    # def validate(self, attrs):
    #     # Convertir cadenas vacías a None
    #     for key, value in attrs.items():
    #         if value == '' or 'null':
    #             attrs[key] = None
    #     print(attrs)
    #     return attrs
    # def validate(self, data):
    #     # Validación personalizada para campos numéricos y fecha
    #     for field in ['edad', 'nivEdu']:
    #         if field in data and data[field] != 'null':
    #             try:
    #                 data[field] = int(data[field]) if data[field] is not None else None
    #             except (ValueError, TypeError):
    #                 data[field] = None

    #     # Validación para fecha
    #     if 'fechaNacimiento' in data and data['fechaNacimiento']:
    #         try:
    #             from datetime import datetime
    #             # Convertir a formato de fecha si es un string
    #             if isinstance(data['fechaNacimiento'], str):
    #                 data['fechaNacimiento'] = datetime.strptime(data['fechaNacimiento'], '%Y-%m-%d').date()
    #         except ValueError:
    #             data['fechaNacimiento'] = None

    #     return data
    
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
        # Actualizar todos los campos que vengan en validated_data
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        return instance
        
    # def validate(self, value):
    #     return value.strftime('%Y-%m-%d') if value else value
    #     for field in ['edad', 'nivEdu']:
    #         if field in data:
    #             try:
    #                 data[field] = int(data[field]) if data[field] != '' else None
    #             except (ValueError, TypeError):
    #                 data[field] = None

    #         if 'fechaNacimiento' in data and data['fechaNacimiento']:
    #             try:
    #                 from datetime import datetime
    #                 datetime.strptime(data['fechaNacimiento'], '%Y-%m-%d')
    #             except ValueError:
    #                 data['fechaNacimiento'] = None

    #     return data