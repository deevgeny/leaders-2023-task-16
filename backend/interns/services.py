from core.exceptions import NotFoundException
from interns.models import InternsRequest
from interns.serializers import InternsRequestSerializer
from staff.models import Organization


class InternsRequestService:
    def create(
        self, organization_id: int, dto: InternsRequestSerializer
    ) -> InternsRequestSerializer:
        try:
            organization = Organization.objects.get(pk=organization_id)
        except Organization.DoesNotExist:
            raise NotFoundException()

        interns_request = InternsRequest.objects.create(
            organization=organization, **dto.validated_data
        )

        interns_request.save()
        return InternsRequestSerializer(interns_request)

    def update(
        self, id: int, dto: InternsRequestSerializer
    ) -> InternsRequestSerializer:
        try:
            interns_request = InternsRequest.objects.get(pk=id)
        except InternsRequest.DoesNotExist:
            raise NotFoundException()

        interns_request.name = dto.validated_data["name"]
        interns_request.description = dto.validated_data["description"]

        interns_request.save()
        return InternsRequestSerializer(interns_request)

    def get_by_id(self, id: int) -> InternsRequestSerializer:
        try:
            interns_request = InternsRequest.objects.get(pk=id)
        except InternsRequest.DoesNotExist:
            raise NotFoundException()

        return InternsRequestSerializer(interns_request)

    def get_organization_requests(
        self, organization_id: int
    ) -> list[InternsRequestSerializer]:
        queryset = InternsRequest.objects.filter(organization__pk=organization_id)
        return list(map(InternsRequestSerializer, queryset))

    def delete(self, id: int):
        try:
            interns_request = InternsRequest.objects.get(pk=id)
        except InternsRequest.DoesNotExist:
            raise NotFoundException()

        interns_request.delete()
