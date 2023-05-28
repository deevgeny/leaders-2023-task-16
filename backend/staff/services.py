from core.exceptions import AlreadyExistsException, NotFoundException
from staff.models import Organization
from staff.serializers import OrganizationSerializer
from users.models import User


class OrganizationService:
    def create(
        self, user_id: int, dto: OrganizationSerializer
    ) -> OrganizationSerializer:
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise NotFoundException()

        if user.organization is not None:
            raise AlreadyExistsException()

        user.organization = Organization.objects.create(**dto.validated_data)
        user.organization.save()
        user.save()
        return OrganizationSerializer(user.organization)

    def update_by_user_id(
        self, user_id: int, dto: OrganizationSerializer
    ) -> OrganizationSerializer:
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise NotFoundException()

        if user.organization is None:
            raise NotFoundException()

        data = dto.validated_data

        user.organization.email = data["email"]
        user.organization.phone = data["phone"]
        user.organization.name = data["name"]
        user.organization.description = data["description"]
        user.organization.address = data["address"]

        user.organization.save()
        user.save()
        return OrganizationSerializer(user.organization)

    def get_by_id(self, id: int) -> OrganizationSerializer:
        try:
            organization = Organization.objects.get(pk=id)
        except Organization.DoesNotExist:
            raise NotFoundException()

        return OrganizationSerializer(organization)

    def get_by_user_id(self, user_id: int) -> OrganizationSerializer:
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise NotFoundException()

        if user.organization is None:
            raise NotFoundException()

        return OrganizationSerializer(user.organization)
