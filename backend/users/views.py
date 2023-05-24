from django.http.response import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.views import APIView

from core.exceptions import PermissionDeniedException
from users.serializers import (
    UserCreateSerializer,
    UserInfoSerializer,
    UserSerializer,
    UserUpdateSerializer,
)
from users.services import UserService


@api_view(['POST'])
def registration(request: Request):
    if not request.user.is_anonymous:
        raise PermissionDeniedException()

    data = JSONParser().parse(request)
    user_dto = UserCreateSerializer(data=data)
    user_dto.is_valid(raise_exception=True)

    user = UserService().register(user_dto)
    return JsonResponse(user.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_by_id(request: Request, user_id: int):
    user = UserService().get_by_id(user_id)
    return JsonResponse(user.data)


class UserMeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request):
        return JsonResponse(UserSerializer(request.user).data)

    def put(self, request: Request):
        data = JSONParser().parse(request)
        user_dto = UserUpdateSerializer(data=data)
        user_dto.is_valid(raise_exception=True)

        user = UserService().update_by_id(request.user.id, user_dto)
        return JsonResponse(user.data)


class UserMeInfoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request):
        info = UserService().get_info_by_id(request.user.id)
        return JsonResponse(data=info.data)

    def post(self, request: Request):
        data = JSONParser().parse(request)
        info_dto = UserInfoSerializer(data=data)
        info_dto.is_valid(raise_exception=True)

        info = UserService().update_info_by_id(request.user.id, info_dto)
        return JsonResponse(info.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_info_by_id(request: Request, user_id: int):
    info = UserService().get_info_by_id(user_id)

    return JsonResponse(info.data)
