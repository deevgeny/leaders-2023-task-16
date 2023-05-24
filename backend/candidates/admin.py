from django.contrib import admin

from candidates.models import CandidateRequest


@admin.register(CandidateRequest)
class CandidateRequestAdmin(admin.ModelAdmin):
    ...
