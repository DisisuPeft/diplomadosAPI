from django.urls import path, re_path
from .views import (
    UsuariosAdministrador,
)



urlpatterns = [

    path('admin/usuarios/', UsuariosAdministrador.as_view()),
    # path('auth/refresh/', CustomTokenRefreshView.as_view()),
    # path('auth/verify/', CustomTokenVerifyView.as_view()),
    # path('auth/register/', RegisterView.as_view()),
    # path('logout/', LogoutView.as_view()),


    # path('auth/user/', ProfileView.as_view()),
    # path('check/user/', CheckUser.as_view()),
]