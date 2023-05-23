from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """Register custom user model on admin site."""
    fieldsets = (
        (_("Данные авторизации"), {"fields": ("email", "password")}),
        (_("Personal info"),
         {"fields": ("first_name", "patronymic", "last_name", "phone",
                     "role")}),
        (_("Анкета кандидата"),
         {"fields": ("birthday", "university_name", "university_year",
                     "job_experience", "skills", "departments")}),
        (_("Permissions"),
         {"fields": ("is_active", "is_staff", "is_superuser", "groups",
                     "user_permissions")}),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {"classes": ("wide",),
                "fields": ("email", "first_name", "patronymic", "last_name",
                           "phone", "password1", "password2",)}),
    )
    list_display = ("id", "email", "first_name", "patronymic", "last_name",
                    "role", "is_active", "is_staff", "is_superuser")
    list_display_links = ("email",)
    list_filter = ("is_staff", "is_active", "is_superuser")
    ordering = ("email",)
