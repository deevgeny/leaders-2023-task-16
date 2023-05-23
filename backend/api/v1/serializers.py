from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserAccountCreateSerializer(serializers.ModelSerializer):
    """Create user account serializer."""

    class Meta:
        model = User
        fields = ["id", "email", "password", "first_name", "patronymic",
                  "last_name", "phone"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserAccountReadSerializer(serializers.ModelSerializer):
    """User account read serializer."""

    class Meta:
        model = User
        fields = ["id", "email", "role", "first_name", "patronymic",
                  "last_name", "phone"]
        read_only_fields = ["id", "email", "role", "first_name", "patronymic",
                            "last_name", "phone"]


class UserAccountUpdateSerializer(serializers.ModelSerializer):
    """User account update serializer."""

    class Meta:
        model = User
        fields = ["id", "email", "password", "first_name", "patronymic",
                  "last_name", "phone"]
        extra_kwargs = {"password": {"required": False, "write_only": True}}


class UserInfoCreateReadUpdateSerializer(serializers.ModelSerializer):
    """User info create/read/update serializer."""

    class Meta:
        model = User
        fields = ["birthday", "university_name", "university_year",
                  "job_experience", "skills", "departments"]
