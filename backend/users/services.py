from core.exceptions import AlreadyExistsException, NotFoundException
from core.utils import set_attrs_from_dict
from users.models import User, UserInfo
from users.serializers import (
    UserCreateSerializer,
    UserInfoSerializer,
    UserSerializer,
    UserUpdateSerializer,
)


class UserService:
    def register(self, user_dto: UserCreateSerializer) -> UserSerializer:
        data = user_dto.validated_data

        if User.objects.filter(email=data["email"]).exists():
            raise AlreadyExistsException()

        user = User.objects.create_user(**data)
        return UserSerializer(user)

    def get_by_id(self, id: int) -> UserSerializer:
        try:
            user = User.objects.get(pk=id)
        except User.DoesNotExist:
            raise NotFoundException()

        return UserSerializer(user)

    def get_info_by_id(self, id: int) -> UserInfoSerializer:
        try:
            user = User.objects.get(pk=id)
        except User.DoesNotExist:
            raise NotFoundException()

        try:
            user_info = UserInfo.objects.get(pk=user)
        except UserInfo.DoesNotExist:
            raise NotFoundException()

        return UserInfoSerializer(user_info)

    def update_by_id(self, id: int, user_dto: UserUpdateSerializer) -> UserSerializer:
        try:
            user: User = User.objects.get(pk=id)
        except UserInfo.DoesNotExist:
            raise NotFoundException()

        data = user_dto.validated_data

        if (
            data["email"] != user.email
            and User.objects.filter(email=data["email"]).exists()
        ):
            raise AlreadyExistsException()

        if "password" in data:
            if data["password"] is not None:
                user.set_password(data["password"])
            data.pop("password")

        set_attrs_from_dict(user, data)

        user.save()
        return UserSerializer(user)

    def update_info_by_id(
        self, id: int, info_dto: UserInfoSerializer
    ) -> UserInfoSerializer:
        try:
            user: User = User.objects.get(pk=id)
        except UserInfo.DoesNotExist:
            raise NotFoundException()

        data = info_dto.validated_data

        try:
            user_info = UserInfo.objects.get(pk=user)
            set_attrs_from_dict(user_info, data)
        except UserInfo.DoesNotExist:
            user_info = UserInfo.objects.create(user=user, **data)

        user_info.save()

        return UserInfoSerializer(user_info)
