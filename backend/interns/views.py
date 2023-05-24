from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from auth.permissions import IsStaff
from core.exceptions import NotFoundException, PermissionDeniedException
from interns.serializers import InternsRequestSerializer
from interns.services import InternsRequestService


class MyOrganizationRequests(APIView):
    permission_classes = [IsStaff]

    def post(self, request):
        if request.user.organization is None:
            raise NotFoundException()

        data = JSONParser().parse(request)
        dto = InternsRequestSerializer(data=data)

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

        return JsonResponse(map(lambda t: t.data, requests), safe=False)


class MyOrganizationRequestById(APIView):
    permission_classes = [IsStaff]

    def put(self, request, id: int):
        if request.user.organization is None:
            raise NotFoundException()

        interns_request = InternsRequestService().get_by_id(id)
        if interns_request.organization.id != request.user.organization.id:
            raise PermissionDeniedException()

        data = JSONParser().parse(request)
        dto = InternsRequestSerializer(data=data)

        interns_request = InternsRequestService().update(id, dto)

        return JsonResponse(interns_request.data)

    def delete(self, request, id: int):
        if request.user.organization is None:
            raise NotFoundException()

        interns_request = InternsRequestService().get_by_id(id)
        if interns_request.organization.id != request.user.organization.id:
            raise PermissionDeniedException()

        InternsRequestService().delete(id)

        return JsonResponse({})
