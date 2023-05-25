from django.http.response import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.views import APIView

from auth.permissions import IsStaff
from core.exceptions import (
    InvalidFormatException,
    NotFoundException,
    PermissionDeniedException,
)
from interns.models import InternsRequest
from interns.serializers import InternsRequestSerializer
from interns.services import InternsRequestService
from users.models import User


class MyOrganizationRequests(APIView):
    permission_classes = [IsStaff]

    def post(self, request):
        if request.user.organization is None:
            raise NotFoundException()

        data = JSONParser().parse(request)
        dto = InternsRequestSerializer(data=data)
        dto.is_valid(raise_exception=True)

        interns_request = InternsRequestService().create(
            request.user.organization.id, dto
        )

        return JsonResponse(interns_request.data)

    def get(self, request):
        if request.user.organization is None:
            raise NotFoundException()

        requests = InternsRequestService().get_organization_requests(
            request.user.organization.id
        )

        return JsonResponse(list(map(lambda t: t.data, requests)), safe=False)


class MyOrganizationRequestById(APIView):
    permission_classes = [IsStaff]

    def put(self, request, id: int):
        if request.user.organization is None:
            raise NotFoundException()

        interns_request = InternsRequestService().get_by_id(id)
        if interns_request.data["organization_id"] != request.user.organization.id:
            raise PermissionDeniedException()

        data = JSONParser().parse(request)
        dto = InternsRequestSerializer(data=data)
        dto.is_valid(raise_exception=True)

        interns_request = InternsRequestService().update(id, dto)

        return JsonResponse(interns_request.data)

    def delete(self, request, id: int):
        if request.user.organization is None:
            raise NotFoundException()

        interns_request = InternsRequestService().get_by_id(id)
        if interns_request.data["organization_id"] != request.user.organization.id:
            raise PermissionDeniedException()

        InternsRequestService().delete(id)

        return JsonResponse({})


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_interns_request_by_id(request, id: int):
    if request.user.organization is None:
        raise PermissionDeniedException()

    interns_request = InternsRequestService().get_by_id(id)
    if interns_request.data["organization_id"] != request.user.organization.id:
        raise PermissionDeniedException()

    return JsonResponse(interns_request.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_interns_requests_list(request: Request):
    raw_page = request.query_params.get("page", "0")
    raw_size = request.query_params.get("size", "10")
    raw_status = request.query_params.get("status", "")

    try:
        page = int(raw_page)
    except ValueError:
        raise InvalidFormatException()

    try:
        size = int(raw_size)
    except ValueError:
        raise InvalidFormatException()

    if len(raw_status) == 0:
        status = None
    elif raw_status in InternsRequest.Status.values:
        status = raw_status
    else:
        raise InvalidFormatException()

    if request.user.role not in [User.Role.CURATOR, User.Role.INTERN]:
        raise PermissionDeniedException()

    if request.user.role == User.Role.INTERN:
        status = InternsRequest.Status.ACCEPTED

    interns_requests = InternsRequestService().get_requests(page, size, status)

    return JsonResponse(list(map(lambda t: t.data, interns_requests)), safe=False)
