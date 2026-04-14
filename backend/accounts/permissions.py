from rest_framework.permissions import BasePermission


class IsHost(BasePermission):
    """
    Allows access only to host users.
    """

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.is_host
        )