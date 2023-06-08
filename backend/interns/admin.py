from django.contrib import admin

from .models import InternIntro


@admin.register(InternIntro)
class InternIntroAdmin(admin.ModelAdmin):
    list_display = ["user", "url", "progress"]
