from rest_framework import serializers

from staff.models import Organization


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ["id", "email", "phone", "name", "description", "address"]
        read_only_fields = ["id"]
