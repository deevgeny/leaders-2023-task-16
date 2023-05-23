from core.exceptions import AlreadyExistsException, NotFoundException
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

        if User.objects.filter(email=data['email']).exists():
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
            user_info = UserInfo.objects.get(user__pk=id)
        except UserInfo.DoesNotExist:
            raise NotFoundException()

        return UserInfoSerializer(user_info)

    def update_by_id(
            self, id: int, user_dto: UserUpdateSerializer
    ) -> UserSerializer:
        try:
            user: User = User.objects.get(pk=id)
        except UserInfo.DoesNotExist:
            raise NotFoundException()

        data = user_dto.validated_data

        if User.objects.filter(email=data['email']).exists():
            raise AlreadyExistsException()

        user.email = data['email']
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.surname = data['surname']
        user.phone = data['phone']

        if user_dto.password is not None:
            user.set_password(user_dto.password)

        user.save()
        return UserSerializer(user)

    def update_info_by_id(self, id: int, info_dto: UserInfoSerializer) -> UserInfoSerializer:
        try:
            user: User = User.objects.get(pk=id)
        except UserInfo.DoesNotExist:
            raise NotFoundException()

        data = info_dto.validated_data

        try:
            user_info = UserInfo.objects.get(user__pk=id)
            user_info.birthdate = data['birthdate']
            user_info.university_name = data['university_name']
            user_info.university_year = data['university_year']
            user_info.job_experience = data['job_experience']
            user_info.skills = data['skills']
            user_info.departments = data['departments']
        except UserInfo.DoesNotExist:
            user_info = UserInfo.objects.create(
                **data
            )
            user_info.user = user

        user_info.save()

        return UserInfoSerializer(user_info)
