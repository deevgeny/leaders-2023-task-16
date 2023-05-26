from rest_framework import serializers

from candidates.models import CandidateRequest
from users.serializers import UserSerializer


class CandidateRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateRequest
        exclude = ["user"]
        read_only_fields = ["status"]


class BriefCandidateRequestSerializer(serializers.Serializer):
    user = UserSerializer()
    status = serializers.CharField()

    class Meta:
        model = CandidateRequest
        fields = ["user", "status"]
