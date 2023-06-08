from django.contrib import admin

from candidates.models import CandidateRequest


@admin.register(CandidateRequest)
class CandidateRequestAdmin(admin.ModelAdmin):
    list_display = ["user", "departments", "internship_source", "schedule",
                    "status"]
    list_filter = ["departments", "status", "schedule"]
