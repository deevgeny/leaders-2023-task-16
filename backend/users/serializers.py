from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from users.models import InternshipState, User, UserInfo


class InternshipStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternshipState
        fields = ["stage", "request_status", "school_status", "test_status",
                  "case_status", "choice_status", "work_status"]


class UserSerializer(serializers.ModelSerializer):

    state = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["id", "email", "role", "first_name", "last_name", "surname",
                  "phone", "state"]

    def get_state(self, obj):
        """Return user state data from one-to-one related model."""
        try:
            if obj.role in [User.Role.CANDIDATE, User.Role.INTERN]:
                return InternshipStateSerializer(obj.state).data
        except ObjectDoesNotExist:
            return None


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password", "first_name", "last_name", "surname",
                  "phone"]


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
        exclude = ["user"]


class BriefUserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ["gender", "birthdate", "citizenship", "education_level",
                  "city"]
