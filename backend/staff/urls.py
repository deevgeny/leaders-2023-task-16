from django.urls import path

from staff.views import (
    MyOrganizationView,
    get_organization_by_id,
    get_organization_statistics,
)

urlpatterns = [
    path("organizations/my/", MyOrganizationView.as_view()),
    path("organizations/<int:organization_id>/", get_organization_by_id),
    path("organizations/statistics/", get_organization_statistics)
]
