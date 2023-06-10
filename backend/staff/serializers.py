from rest_framework import serializers

from staff.models import Organization


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ["id", "email", "phone", "name", "description", "address"]
        read_only_fields = ["id"]


class OrganizationStatisticsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    total_requests_count = serializers.IntegerField()
    waiting_requests_count = serializers.IntegerField()
    accepted_requests_count = serializers.IntegerField()
    declined_requests_count = serializers.IntegerField()
