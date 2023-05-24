from rest_framework import serializers

from candidates.models import CandidateRequest
from users.serializers import UserSerializer


class CandidateRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateRequest
        fields = ["score_percentage", "status"]
        read_only_fields = ["score_percentage", "status"]


class VerboseCandidateRequestSerializer(serializers.Serializer):
    user = UserSerializer()
    score_percentage = serializers.IntegerField()
    status = serializers.CharField()

    class Meta:
        model = CandidateRequest
        fields = ["user", "score_percentage", "status"]
