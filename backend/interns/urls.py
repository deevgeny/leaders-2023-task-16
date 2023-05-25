from django.urls import path

from interns.views import (
    MyOrganizationRequestById,
    MyOrganizationRequests,
    get_interns_request_by_id,
    get_interns_requests_list,
)

urlpatterns = [
    path("organizations/my/requests", MyOrganizationRequests.as_view()),
    path("organizations/my/requests/<int:id>", MyOrganizationRequestById.as_view()),
    path("requests/<int:id>", get_interns_request_by_id),
    path("requests/", get_interns_requests_list),
]
