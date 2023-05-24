from django.urls import path

from interns.views import MyOrganizationRequestById, MyOrganizationRequests

urlpatterns = [
    path("organization/my/requests", MyOrganizationRequests.as_view()),
    path("organization/my/requests/<int:id>", MyOrganizationRequestById.as_view()),
]
