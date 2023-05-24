from rest_framework import serializers

from users.models import User, UserInfo


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "role", "first_name", "last_name", "surname", "phone"]


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password", "first_name", "last_name", "surname", "phone"]


class UserUpdateSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(required=False, allow_null=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    surname = serializers.CharField()
    phone = serializers.CharField()


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = [
            "birthdate",
            "university_name",
            "university_year",
            "job_experience",
            "skills",
            "departments",
            "citizenship",
        ]
