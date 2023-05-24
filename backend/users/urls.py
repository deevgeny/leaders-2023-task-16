from django.urls import path

from users.views import (
    UserMeInfoView,
    UserMeView,
    get_info_by_id,
    get_user_by_id,
    registration,
)

urlpatterns = [
    path('registration', registration),
    path('users/me', UserMeView.as_view()),
    path('users/<int:user_id>', get_user_by_id),
    path('users/me/info', UserMeInfoView.as_view()),
    path('users/<int:user_id>/info', get_info_by_id)
]
