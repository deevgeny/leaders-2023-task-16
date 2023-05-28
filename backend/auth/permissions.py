from rest_framework.permissions import BasePermission

from users.models import User


class HasRolePermission(BasePermission):
    ROLE: User.Role

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == self.ROLE


class IsCandidate(HasRolePermission):
    ROLE = User.Role.CANDIDATE


class IsIntern(HasRolePermission):
    ROLE = User.Role.INTERN


class IsCurator(HasRolePermission):
    ROLE = User.Role.CURATOR


class IsStaff(HasRolePermission):
    ROLE = User.Role.STAFF


class IsMentor(HasRolePermission):
    ROLE = User.Role.MENTOR
