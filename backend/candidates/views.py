from django.http.response import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.request import Request
from rest_framework.views import APIView

from auth.permissions import IsCandidate, IsCurator
from candidates.services import CandidatesService
from core.exceptions import InvalidFormatException


class CandidatesMeRequestView(APIView):
    permission_classes = [IsCandidate]

    def post(self, request):
        candidate_request = CandidatesService().create(request.user.id)
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
