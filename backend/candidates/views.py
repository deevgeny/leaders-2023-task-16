from django.contrib.auth import get_user_model
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CandidateCareerSchool, CandidateRequest, CandidateTest
from auth.permissions import IsCandidate, IsCurator
from candidates.serializers import (
    CandidateCareerSchoolSerializer,
    CandidateRequestSerializer,
    CandidateStatisticsSerializer,
    CandidateTestSerializer,
)
from candidates.services import CandidatesService
from core.exceptions import InvalidFormatException

User = get_user_model()


class CandidatesMeRequestView(APIView):
    permission_classes = [IsCandidate]

    def post(self, request):
        data = JSONParser().parse(request)

        dto = CandidateRequestSerializer(data=data)
        dto.is_valid(raise_exception=True)

        candidate_request = CandidatesService().create(request.user.id, dto)
        return JsonResponse(candidate_request.data)

    def get(self, request):
        candidate_request = CandidatesService().get(request.user.id)
        return JsonResponse(candidate_request.data)


@api_view(["GET"])
@permission_classes([IsCurator])
def search_candidates(request: Request):
    try:
        page_number = int(request.query_params.get("page", "0"))
    except ValueError:
        raise InvalidFormatException()

    try:
        page_size = int(request.query_params.get("size", "10"))
    except ValueError:
        raise InvalidFormatException()

    raw_recommended = request.query_params.get("recommended")
    if raw_recommended is not None:
        recommended = raw_recommended.lower() == "true"
    else:
        recommended = None

    results = CandidatesService().search(page_number, page_size, recommended)

    return JsonResponse(list(map(lambda t: t.data, results)), safe=False)


@api_view(["GET"])
@permission_classes([IsCurator])
def get_candidate_request_by_id(request, user_id: int):
    candidate_request = CandidatesService().get(user_id)
    return JsonResponse(candidate_request.data)


@api_view(["POST"])
@permission_classes([IsCurator])
def accept_candidate_request(request, user_id: int):
    CandidatesService().accept(user_id)
    return JsonResponse({})


@api_view(["POST"])
@permission_classes([IsCurator])
def decline_candidate_request(request, user_id: int):
    CandidatesService().decline(user_id)
    return JsonResponse({})


class CandidateCareerSchoolView(APIView):
    permission_classes = [IsCandidate]

    def get(self, request):
        obj = get_object_or_404(CandidateCareerSchool, user=request.user)
        serializer = CandidateCareerSchoolSerializer(obj)
        return Response(serializer.data)


class CandidateTestView(APIView):
    permission_classes = [IsCandidate]

    def get(self, request):
        obj = get_object_or_404(CandidateTest, user=request.user)
        serializer = CandidateTestSerializer(obj)
        return Response(serializer.data)


class CandidatesStatistics(APIView):
    permission_classes = [IsCurator]

    def get(self, request):
        queryset = (CandidateRequest.objects
                    .filter(user__role=User.Role.CANDIDATE)
                    .select_related("user", "user__info", "user__state")
                    .all())
        serializer = CandidateStatisticsSerializer(queryset)
        return Response(serializer.data)
