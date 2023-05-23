from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import generics, status, views
from rest_framework.response import Response

from .permissions import (
    AnonymousUserRegistration,
    AuthenticatedReadOnly,
    CreateReadUpdateUserInfo,
    ReadUpdatePersonalUserAccount,
)
from .serializers import (
    UserAccountCreateSerializer,
    UserAccountReadSerializer,
    UserAccountUpdateSerializer,
    UserInfoCreateReadUpdateSerializer,
)

User = get_user_model()


class UserRegistrationView(generics.CreateAPIView):
    """User registration view for anonymous users."""
    queryset = User.objects.all()
    serializer_class = UserAccountCreateSerializer
    permission_classes = [AnonymousUserRegistration]


class UserAccountReadUpdateView(generics.RetrieveUpdateAPIView):
    """Read or update user personal account view."""
    queryset = User.objects.all()
    permission_classes = [ReadUpdatePersonalUserAccount]

    def get_object(self):
        return get_object_or_404(self.get_queryset(), id=self.request.user.id)

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return UserAccountUpdateSerializer
        return UserAccountReadSerializer


class UserAccountDetailsView(generics.RetrieveAPIView):
    """User account details view by user id."""
    queryset = User.objects.all()
    lookup_field = "id"
    serializer_class = UserAccountReadSerializer
    permission_classes = [AuthenticatedReadOnly]


class UserInfoDetailsView(generics.RetrieveAPIView):
    """User info details view by user id."""
    queryset = User.objects.all()
    lookup_field = "id"
    serializer_class = UserInfoCreateReadUpdateSerializer
    permission_classes = [AuthenticatedReadOnly]


class UserInfoCreateReadUpdateView(views.APIView):
    """User info create/read/update view."""
    permission_classes = [CreateReadUpdateUserInfo]

    def get(self, request):
        obj = get_object_or_404(User, id=request.user.id)
        serializer = UserInfoCreateReadUpdateSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        obj = get_object_or_404(User, id=request.user.id)
        serializer = UserInfoCreateReadUpdateSerializer(instance=obj,
                                                        data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
