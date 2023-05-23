from django.contrib.auth import get_user_model
from rest_framework import permissions

User = get_user_model()


class AnonymousUserRegistration(permissions.BasePermission):
    """Registration permission for anonymous user."""

    def has_permission(self, request, view):
        return request.method == "POST" and request.user.is_anonymous


class ReadUpdatePersonalUserAccount(permissions.BasePermission):
    """Read and update personal user account data."""

    def has_permission(self, request, view):
        return (request.method in ["GET", "PUT"]
                and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return request.user.id == obj.id


class AuthenticatedReadOnly(permissions.BasePermission):
    """Read only permission for authenticated users."""

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                and request.user.is_authenticated)


class CreateReadUpdateUserInfo(permissions.BasePermission):
    """Create/read/update personal user info data."""

    def has_permission(self, request, view):
        return (request.method in ["GET", "POST"]
                and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return request.user.id == obj.id
