from django.urls import path

from candidates.views import (
    CandidateCareerSchoolView,
    CandidatesMeRequestView,
    CandidatesStatisticsView,
    CandidateTestView,
    accept_candidate_request,
    decline_candidate_request,
    get_candidate_request_by_id,
    search_candidates,
)

urlpatterns = [
    path("candidates/me/request/", CandidatesMeRequestView.as_view()),
    path("candidates/me/school/", CandidateCareerSchoolView.as_view()),
    path("candidates/me/test/", CandidateTestView.as_view()),
    path("candidates/requests/", search_candidates),
    path("candidates/<int:user_id>/request/", get_candidate_request_by_id),
    path("candidates/<int:user_id>/accept/", accept_candidate_request),
    path("candidates/<int:user_id>/decline/", decline_candidate_request),
    path("statistics/candidates/", CandidatesStatisticsView.as_view())
]
