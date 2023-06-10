from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from auth.permissions import IsCurator, IsIntern, IsStaff
from core.exceptions import (
    InvalidFormatException,
    NotFoundException,
    PermissionDeniedException,
)
from interns.models import InternCase, InternsRequest
from interns.serializers import (
    InternCaseSerializer,
    InternsRequestSerializer,
    RequestsStatisticsSerializer,
)
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
        if (interns_request.data["organization_id"]
                != request.user.organization.id):
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
        if (interns_request.data["organization_id"]
                != request.user.organization.id):
            raise PermissionDeniedException()

        InternsRequestService().delete(id)

        return JsonResponse({})


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_interns_request_by_id(request, id: int):
    interns_request = InternsRequestService().get_by_id(id)

    if request.user.role == User.Role.STAFF and (
        request.user.organization is None
        or interns_request.data["organization_id"]
        != request.user.organization.id
    ):
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

    if request.user.role in [
        User.Role.INTERN,
        User.Role.CANDIDATE,
        User.Role.STAFF,
        User.Role.MENTOR,
    ]:
        status = InternsRequest.Status.ACCEPTED

    interns_requests = InternsRequestService().get_requests(page, size, status)

    return JsonResponse(
        list(map(lambda t: t.data, interns_requests)), safe=False
    )


@api_view(["POST"])
@permission_classes([IsCurator])
def accept_interns_request(request, id: int):
    interns_request = InternsRequestService().accept(id)
    return JsonResponse(interns_request.data)


@api_view(["POST"])
@permission_classes([IsCurator])
def decline_interns_request(request, id: int):
    interns_request = InternsRequestService().decline(id)
    return JsonResponse(interns_request.data)


class InternCaseView(APIView):
    permission_classes = [IsIntern]

    def get(self, request):
        obj = get_object_or_404(InternCase, user=request.user)
        # Pass request to build full url path to solution file
        serializer = InternCaseSerializer(instance=obj,
                                          context={"request": request})
        return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsCurator])
def get_interns_requests_statistics(request):
    stats = InternsRequestService().get_statistics()
    return JsonResponse(stats.initial_data)
