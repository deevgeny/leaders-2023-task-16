from rest_framework import serializers

from candidates.models import (
    CandidateCareerSchool,
    CandidateRequest,
    CandidateTest,
)
from users.serializers import BriefUserInfoSerializer, UserSerializer


class CandidateRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateRequest
        exclude = ["user"]
        read_only_fields = ["status"]


class BriefCandidateRequestSerializer(serializers.Serializer):
    user = UserSerializer()
    info = BriefUserInfoSerializer(source="user.info")
    departments = serializers.CharField()
    status = serializers.CharField()

    class Meta:
        model = CandidateRequest
        fields = [
            "user",
            "info",
            "departments",
            "status",
        ]


class CandidateCareerSchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateCareerSchool
        fields = ["url", "progress"]


class CandidateTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateTest
        fields = ["url", "status"]
