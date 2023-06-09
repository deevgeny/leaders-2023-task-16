from django.contrib import admin

from users.models import InternshipState, User, UserInfo


class UserInfoInline(admin.StackedInline):
    model = UserInfo


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ["email"]}),
        ("Личные данные",
         {"fields": ["last_name", "first_name", "surname", "phone"]}),
        ("Права доступа",
         {"fields": ["role", "is_superuser", "groups", "user_permissions"]},),
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
