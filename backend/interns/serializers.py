from rest_framework import serializers

from .models import InternCase, InternsRequest


class InternsRequestSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    test = serializers.CharField()
    organization_id = serializers.IntegerField(source="organization.id",
                                               read_only=True)
    status = serializers.CharField(read_only=True)

    class Meta:
        model = InternsRequest
        fields = ["id", "name", "description", "test", "organization_id",
                  "status"]
        read_only_fields = ["id", "organization_id", "status"]


class InternCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternCase
        fields = ["name", "description", "solution", "status"]
