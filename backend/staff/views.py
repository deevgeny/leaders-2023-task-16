from django.http.response import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from auth.permissions import IsStaff
from core.exceptions import PermissionDeniedException
from staff.serializers import OrganizationSerializer
from staff.services import OrganizationService
from users.models import User


class MyOrganizationView(APIView):
    permission_classes = [IsStaff]

    def post(self, request):
        data = JSONParser().parse(request)
        dto = OrganizationSerializer(data=data)
        dto.is_valid(raise_exception=True)

        organization = OrganizationService().create(request.user.id, dto)

        return JsonResponse(organization.data)

    def put(self, request):
        data = JSONParser().parse(request)
        dto = OrganizationSerializer(data=data)
        dto.is_valid(raise_exception=True)

        organization = OrganizationService().update_by_user_id(request.user.id, dto)

        return JsonResponse(organization.data)

    def get(self, request):
        organization = OrganizationService().get_by_user_id(request.user.id)
        return JsonResponse(organization.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_organization_by_id(request, organization_id: int):
    if request.user.role == User.Role.CANDIDATE:
        raise PermissionDeniedException()

    if (
        request.user.role == User.Role.STAFF
        and request.user.organization is not None
        and request.user.organization.id != organization_id
    ):
        raise PermissionDeniedException()

    organization = OrganizationService().get_by_id(organization_id)

    return JsonResponse(organization.data)
