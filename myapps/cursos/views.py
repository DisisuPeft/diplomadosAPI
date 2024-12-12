from django.shortcuts import render
from rest_framework.views import APIView
from myapps.authentication.permissions import HasRoleWithRoles
from myapps.authentication.models import UserCustomize
from myapps.authentication.serializers import UserCustomizeSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, status
from myapps.cursos.models import Category, SubCategory, Especification
from myapps.cursos.serializers import (
    CategorySerializer,
    SubCategorySerializer,
    EspecificationSerializer,
)

# Create your views here.


class CategoryView(APIView):
    permission_classes = [
        IsAuthenticated,
        HasRoleWithRoles(["Administrador"]),
    ]  # aca tal vez el rol de tutores academicos

    def get(self, request):
        category = Category.objects.all()
        if not category:
            return Response(
                {"error": "No existen categorias disponibles"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = CategorySerializer(category, many=True)
        return Response({"categorys": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        category_dict = {
            "name": request.data["nameCategory"],
            "description": request.data["description"],
        }

        category_serializer = CategorySerializer(data=category_dict)
        if category_serializer.is_valid():
            category = category_serializer.save()
            # return Response(
            #     {"detail": category},
            #     status=status.HTTP_400_BAD_REQUEST,
            # )
            subcategory_dict = {
                "name": request.data["namesubCategory"],
                "category": category.id,
            }
            subcategory = SubCategorySerializer(data=subcategory_dict)
            if subcategory.is_valid():
                instance_subcategory = subcategory.save()
                especification = request.data["especification"].split(",")
                print(instance_subcategory.id)
                for row in range(len(especification)):
                    esp = EspecificationSerializer(
                        data={
                            "name": especification[row],
                            "subcategory": instance_subcategory.id,
                        }
                    )
                    if esp.is_valid():
                        esp.save()
                return Response(
                    {"detail": "data"},
                    status=status.HTTP_200_OK,
                )
        else:
            return Response(
                {"detail": category_serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def patch(self, request):
        category_id = int(request.query_params.get("category_id"))
        sub = request.data["namesubCategory"].split(",")
        esp = request.data["especification"].split(",")

        category = Category.objects.get(id=category_id)
        if not category:
            return Response(
                {"detail": "Categoria no encontrada"},
                status=status.HTTP_200_OK,
            )
        category_serializer = CategorySerializer(
            category,
            data={
                "name": request.data["nameCategory"],
                "description": request.data["description"],
            },
        )
        if category_serializer.is_valid():
            subca = SubCategory.objects.filter(category=category.id)
            # print(subca)
            if not subca:
                return Response(
                    {"detail": "Subcategoria no encontrada"},
                    status=status.HTTP_404_NOT_FOUND,
                )
            for s in subca:
                for row in range(len(sub)):
                    subcategory_serializer = SubCategorySerializer(
                        s, data={"name": sub[row], "category": category.id}
                    )
                    if subcategory_serializer.is_valid():
                        pass
                    else:
                        return Response(
                            {"detail": subcategory_serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST,
                        )
            first_subcategory = subca.first()
            # esp_instance = Especification.objects.filter(subcategory=one.id)
            # en este caso porque solo existe una sola subcategoria pero cuando existan mas? en ese caso va a suceder
            # if not esp_instance:
            #     return Response(
            #         {"detail": "Especificacion(es) no encontrada(s)"},
            #         status=status.HTTP_404_NOT_FOUND,
            #     )
            # for row1 in range(len(esp)):
            #     espec = EspecificationSerializer(esp_instance, data={"name": esp[row1]})
            #     if espec.is_valid():
            #         pass
            #     else:
            #         return Response(
            #             {"detail": espec.errors},
            #             status=status.HTTP_400_BAD_REQUEST,
            #         )
            # category_serializer.save()
            # subcategory_serializer.save()
            # espec.save()
        # print(category_serializer.id)
        else:
            return Response(
                {"detail": category_serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(
            {"detail": "Categorias actualizadas"},
            status=status.HTTP_200_OK,
        )
