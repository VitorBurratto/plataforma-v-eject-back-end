from rest_framework import permissions

class IsAccountOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an account to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Só permite editar, excluir ou visualizar a conta se o usuário for o dono da conta
        return obj.user == request.user