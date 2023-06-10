from django.urls import path

from interns.views import (
    InternCaseView,
    MyOrganizationRequestById,
    MyOrganizationRequests,
    accept_interns_request,
    decline_interns_request,
    get_interns_request_by_id,
    get_interns_requests_list,
    get_interns_requests_statistics,
)

urlpatterns = [
    path("organizations/my/requests/", MyOrganizationRequests.as_view()),
    path("organizations/my/requests/<int:id>/",
         MyOrganizationRequestById.as_view()),
    path("requests/<int:id>/", get_interns_request_by_id),
    path("requests/", get_interns_requests_list),
    path("requests/<int:id>/accept/", accept_interns_request),
    path("requests/<int:id>/decline/", decline_interns_request),
    path("requests/statistics/", get_interns_requests_statistics),
    path("interns/me/case/", InternCaseView.as_view()),
]
