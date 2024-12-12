from myapps.authentication.models import UserCustomize, Roles, Permissions
from rest_framework import serializers
from myapps.perfil.models import Profile
from myapps.perfil.serializers import ProfileSerializer
from django.db import transaction
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from rest_framework import exceptions
from myapps.cursos.models import Category, SubCategory, Especification


class EspecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especification
        fields = ["name", "subcategory"]

    def create(self, validated_data):
        subca = validated_data.pop("subcategory", None)
        esp = Especification.objects.create(**validated_data)
        if subca:
            esp.subcategory = subca
            esp.save()
        return esp

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        return instance


class SubCategorySerializer(serializers.ModelSerializer):
    especification = EspecificationSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = SubCategory
        fields = ["name", "category", "especification"]

    def create(self, validated_data):
        category = validated_data.pop("category", None)
        sub_category = SubCategory.objects.create(**validated_data)
        if category:
            sub_category.category = category
            sub_category.save()
        return sub_category

    def update(self, instance, validated_data):
        print(instance.name)
        instance.name = validated_data.get("name", instance.name)
        instance.category = validated_data.get("category", instance.category)
        return instance


class CategorySerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer(many=True, required=False, read_only=True)

    class Meta:
        model = Category
        fields = ["id", "name", "description", "subcategory"]

    def create(self, validated_data):
        # print(valideted_data)
        category = Category.objects.create(**validated_data)
        return category

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)
        return instance

    # revisar
    # def update(self, instance, validated_data):
    #     # Actualizar todos los campos que vengan en validated_data
    #     # print(instance)
    #     for attr, value in validated_data.items():
    #         setattr(instance, attr, value)

    #     instance.save()
    #     return instance
