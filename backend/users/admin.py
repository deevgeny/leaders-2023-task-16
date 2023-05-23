from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

# @admin.register(User)
# class UserAdmin(UserAdmin):
#     fieldsets = (
#         ("Данные авторизации", {"fields": ("email", "password")}),
#         ("Личная информация",
#          {"fields": ("first_name", "patronymic", "last_name", "phone",
#                      "role")}),
#         ("Права доступа", {"fields": ("is_admin")}),
#     )
#     add_fieldsets = (
#         (None, {"classes": ("wide",),
#                 "fields": ("email", "first_name", "patronymic", "last_name",
#                            "phone", "password1", "password2",)}),
#     )
#     list_display = ("id", "email", "first_name", "patronymic", "last_name",
#                     "role", "is_admin")
#     list_display_links = ("email",)
#     list_filter = ("is_admin")
#     ordering = ("email",)
