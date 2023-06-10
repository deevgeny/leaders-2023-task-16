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


# class RequestsStatisticsSerializer(serializers.Serializer):
#    total_requests_count = serializers.IntegerField()
#    waiting_requests_count = serializers.IntegerField()
#    accepted_requests_count = serializers.IntegerField()
#    declined_requests_count = serializers.IntegerField()


class RequestsStatisticsSerializer(serializers.Serializer):

    total = serializers.SerializerMethodField()
    accepted = serializers.SerializerMethodField()
    declined = serializers.SerializerMethodField()
    recommended = serializers.SerializerMethodField()

    def get_total(self, queryset):
        return len(queryset)

    def get_accepted(self, queryset):
        return queryset.filter(status=CandidateRequest.Status.ACCEPTED).count()

    def get_declined(self, queryset):
        return queryset.filter(status=CandidateRequest.Status.DECLINED).count()

    def get_recommended(self, queryset):
        start_date = datetime.now() - timedelta(days=35 * 365)
        end_date = datetime.now() - timedelta(days=18 * 365)
        return queryset.filter(
            Q(user__info__citizenship__iexact="Российская федерация")
            | Q(user__info__citizenship__iexact="Россия")
            | Q(user__info__citizenship__iexact="РФ"),
            Q(user__info__has_job_experience=True)
            | Q(user__info__has_volunteer_experience=True),
            Q(user__info__education_level__iexact=("высшее образование - "
                                                   "бакалавриат"))
            | Q(user__info__education_level__iexact=("высшее образование "
                                                     "- специалитет, "
                                                         "магистратура")),

            user__info__birthdate__range=(start_date, end_date),
            user__info__graduation_year__lte=datetime.now().year + 3,
        ).count()


class InternsStatisticsSerializer(serializers.Serializer):
    requests = serializers.SerializerMethodField()
    age = serializers.SerializerMethodField()
    gender = serializers.SerializerMethodField()
    directions = serializers.SerializerMethodField()
    education = serializers.SerializerMethodField()
    city = serializers.SerializerMethodField()
    schedule = serializers.SerializerMethodField()
    jobExperience = serializers.SerializerMethodField()

    def get_requests(self, queryset):
        return RequestsStatisticsSerializer(queryset).data
    
    def get_age(self, queryset):
        return {"under18": 1, "between18And25": 5,
                "between25And35": 8, "over35": 5, "average": 28}

    def get_gender(self, queryset):
        return {"male": 8, "female": 4}
    
    def get_directions(self, queryset):
        return [{"name": "HR", "value": 2},
                {"name": "IT", "value": 2},
                {"name": "ГЭ", "value": 9},
                {"name": "КГС", "value": 1},
                {"name": "МГ", "value": 9},
                {"name": "ПП", "value": 2},
                {"name": "СГ", "value": 5}]
    
    def get_education(self, queryset):
        return [{"name": "среднее профессиональное образование",
                       "value": 2},
                      {"name": "высшее образование - бакалавриат",
                       "value": 4},
                      {"name": ("высшее образование - "
                                "специалитет, магистратура"),
                       "value": 5}]
    
    def get_city(self, queryset):
        return {"moscow": 10, "other": 2}
    
    def get_schedule(self, queryset):
        return {"fullTime": 67, "partTime": 32}
    
    def get_jobExperience(self, queryset):
        return {"volunteerExperience": 54, "workExperience": 93}
