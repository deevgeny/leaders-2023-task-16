from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from . import views

urlpatterns = [
    path("token/create/", jwt_views.TokenObtainPairView.as_view(),
         name="create-jwt"),
    path("token/refresh/", jwt_views.TokenRefreshView.as_view(),
         name="refresh-jwt"),
    path("token/validate/", jwt_views.TokenVerifyView.as_view(),
         name="validate-jwt"),
    path("registration/", views.UserRegistrationView.as_view(),
         name="user-registration"),
    path("users/me/", views.UserAccountReadUpdateView.as_view(),
         name="user-account"),
    path("users/<int:id>/", views.UserAccountDetailsView.as_view(),
         name="user-details"),
    path("users/me/info/", views.UserInfoCreateReadUpdateView.as_view(),
         name="user-account-info"),
    path("users/<int:id>/info/", views.UserInfoDetailsView.as_view(),
         name="user-info")
]
