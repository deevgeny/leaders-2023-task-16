from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import InternshipState, User, UserInfo


class UserInfoInline(admin.StackedInline):
    model = UserInfo


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ("Личные данные",
         {'fields': ('first_name', 'surname', 'last_name', 'phone')}),
        ("Права доступа",
         {"fields": ["role", "is_superuser", "groups", "user_permissions"]},),
    )

    add_fieldsets = (
        (None, {"classes": ("wide",),
                "fields": ("email", "first_name", "surname", "last_name",
                           "password1", "password2")}),
    )

    inlines = [UserInfoInline]
    list_display = (
        "id",
        "email",
        "last_name",
        "first_name",
        "surname",
        "role",
        "is_superuser",
    )
    list_display_links = ("email",)
    list_filter = ("role", "is_superuser")
    ordering = ("email",)


@admin.register(InternshipState)
class InternshipStateAdmin(admin.ModelAdmin):
    list_display = ["user", "stage", "request_status", "school_status",
                    "test_status", "case_status", "choice_status",
                    "work_status"]
    list_filter = ["stage", "request_status", "test_status", "case_status",
                   "choice_status", "work_status"]
