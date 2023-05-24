from interns.models import InternsRequest
from rest_framework import serializers


class InternsRequestSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    organization_id = serializers.IntegerField(source="organization.id")
    status = serializers.CharField()

    class Meta:
        model = InternsRequest
        fields = ["id", "name", "description", "organization_id", "status"]
        read_only_fields = ["id", "organization_id", "status"]
