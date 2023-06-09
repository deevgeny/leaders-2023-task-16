from django.contrib import admin

from staff.models import Organization
from users.models import User


class UserInline(admin.StackedInline):
    model = User


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "email", "phone", "address"]
