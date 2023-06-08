from django.contrib import admin

from .models import InternCase


@admin.register(InternCase)
class InternCaseAdmin(admin.ModelAdmin):
    list_display = ["user", "name", "description", "solution", "status"]
    list_filter = ["status"]
