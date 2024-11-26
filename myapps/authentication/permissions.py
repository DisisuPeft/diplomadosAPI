from rest_framework.permissions import BasePermission

class HasRole(BasePermission):
    def __init__(self, allowed_roles=None):
        self.allowed_roles = allowed_roles or []
    
    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated:
            return False
        return user.roleID.filter(name__in=self.allowed_roles).exists()