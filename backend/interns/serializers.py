from datetime import datetime, timedelta

from django.db.models import Q
from rest_framework import serializers

from .models import InternCase, InternsRequest
from candidates.models import CandidateRequest


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


class RequestsStatisticsSerializer(serializers.Serializer):
    total_requests_count = serializers.IntegerField()
    waiting_requests_count = serializers.IntegerField()
    accepted_requests_count = serializers.IntegerField()
    declined_requests_count = serializers.IntegerField()


class PeopleStatisticsSerializer(serializers.Serializer):

    total = serializers.SerializerMethodField()

    def get_total(self, queryset):
        return len(queryset)


class InternsStatisticsSerializer(serializers.Serializer):
    people = serializers.SerializerMethodField()
    age = serializers.SerializerMethodField()
    gender = serializers.SerializerMethodField()
    directions = serializers.SerializerMethodField()
    education = serializers.SerializerMethodField()
    city = serializers.SerializerMethodField()
    schedule = serializers.SerializerMethodField()
    jobExperience = serializers.SerializerMethodField()

    def get_people(self, queryset):
        return PeopleStatisticsSerializer(queryset).data
    
    def get_age(self, queryset):
        return {"under18": 0, "between18And25": 0,
                "between25And35": 1, "over35": 0, "average": 28}

    def get_gender(self, queryset):
        return {"male": 1, "female": 0}
    
    def get_directions(self, queryset):
        return [{"name": "HR", "value": 0},
                {"name": "IT", "value": 1},
                {"name": "ГЭ", "value": 0},
                {"name": "КГС", "value": 0},
                {"name": "МГ", "value": 0},
                {"name": "ПП", "value": 0},
                {"name": "СГ", "value": 0}]
    
    def get_education(self, queryset):
        return [{"name": "среднее профессиональное образование",
                       "value": 0},
                      {"name": "высшее образование - бакалавриат",
                       "value": 0},
                      {"name": ("высшее образование - "
                                "специалитет, магистратура"),
                       "value": 1}]
    
    def get_city(self, queryset):
        return {"moscow": 1, "other": 0}
    
    def get_schedule(self, queryset):
        return {"fullTime": 1, "partTime": 0}
    
    def get_jobExperience(self, queryset):
        return {"volunteerExperience": 1, "workExperience": 1}
