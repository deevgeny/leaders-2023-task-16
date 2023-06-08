from django.contrib import admin

from .models import CandidateCareerSchool, CandidateRequest, CandidateTest


@admin.register(CandidateRequest)
class CandidateRequestAdmin(admin.ModelAdmin):
    list_display = ["user", "departments", "internship_source", "schedule",
                    "status"]
    list_filter = ["departments", "status", "schedule"]


@admin.register(CandidateCareerSchool)
class CandidateCareerSchoolAdmin(admin.ModelAdmin):
    list_display = ["user", "url", "progress"]


@admin.register(CandidateTest)
class CandidateTestAdmin(admin.ModelAdmin):
    list_display = ["user", "url", "status"]
    list_filter = ["status"]
