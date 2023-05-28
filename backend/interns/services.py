from core.exceptions import IntegrityBreachException, NotFoundException
from core.utils import set_attrs_from_dict
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

        if interns_request.status != InternsRequest.Status.WAITING:
            raise IntegrityBreachException()

        set_attrs_from_dict(interns_request, dto.validated_data)

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

    def get_requests(
        self, page: int, size: int, status: InternsRequest.Status | None
    ) -> list[InternsRequestSerializer]:
        queryset = InternsRequest.objects.all()
        if status is not None:
            queryset = queryset.filter(status=status)

        start = page * size
        end = (page + 1) * size

        return list(map(InternsRequestSerializer, queryset[start:end]))

    def delete(self, id: int):
        try:
            interns_request = InternsRequest.objects.get(pk=id)
        except InternsRequest.DoesNotExist:
            raise NotFoundException()

        interns_request.delete()

    def set_status(self, id: int, status: InternsRequest.Status):
        try:
            interns_request = InternsRequest.objects.get(pk=id)
        except InternsRequest.DoesNotExist:
            raise NotFoundException()

        if interns_request.status != InternsRequest.Status.WAITING:
            raise IntegrityBreachException()

        interns_request.status = status
        interns_request.save()

        return InternsRequestSerializer(interns_request)

    def accept(self, id: int):
        return self.set_status(id, InternsRequest.Status.ACCEPTED)

    def decline(self, id: int):
        return self.set_status(id, InternsRequest.Status.DECLINED)
