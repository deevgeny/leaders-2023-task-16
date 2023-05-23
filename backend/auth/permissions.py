from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.views import View


class IsAnonymous(BasePermission):
    def has_permission(self, request: Request, view: View):
        return request.user is None
