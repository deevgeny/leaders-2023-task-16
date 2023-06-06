from datetime import datetime, timedelta

from django.db.models import Q

from candidates.models import CandidateRequest
from candidates.serializers import (
    BriefCandidateRequestSerializer,
    CandidateRequestSerializer,
)
from core.exceptions import (
    AlreadyExistsException,
    IntegrityBreachException,
    NotFoundException,
)
from users.models import User


class CandidatesService:
    def create(
        self, user_id: int, dto: CandidateRequestSerializer
    ) -> CandidateRequestSerializer:
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise NotFoundException()

        if hasattr(user, "candidate_request"):
            raise AlreadyExistsException()

        candidate_request = CandidateRequest.objects.create(
            user=user, **dto.validated_data
        )

        candidate_request.save()
        return CandidateRequestSerializer(candidate_request)

    def get(self, user_id: int) -> CandidateRequestSerializer:
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise NotFoundException()

        try:
            candidate_request = CandidateRequest.objects.get(pk=user)
        except CandidateRequest.DoesNotExist:
            raise NotFoundException()

        return CandidateRequestSerializer(candidate_request)

    def search(
        self, page: int, size: int, recommended: bool | None
    ) -> list[BriefCandidateRequestSerializer]:
        start, end = page * size, (page + 1) * size

        queryset = CandidateRequest.objects.filter(
            status=CandidateRequest.Status.WAITING
        )

        if recommended:
            start_date = datetime.now() - timedelta(days=35 * 365)
            end_date = datetime.now() - timedelta(days=18 * 365)

            queryset = queryset.filter(
                Q(user__info__citizenship__iexact="Российская федерация")
                | Q(user__info__citizenship__iexact="Россия")
                | Q(user__info__citizenship__iexact="РФ"),

                Q(user__info__has_job_experience=True)
                | Q(user__info__has_volunteer_experience=True),

                user__info__birthdate__range=(start_date, end_date),
                user__info__graduation_year__lte=datetime.now().year + 3
            )

        queryset = queryset.order_by("pk")

        return list(map(BriefCandidateRequestSerializer, queryset[start:end]))

    def set_request_status(self, user_id: int, status: CandidateRequest.Status):
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise NotFoundException()

        try:
            candidate_request = CandidateRequest.objects.get(pk=user)
        except CandidateRequest.DoesNotExist:
            raise NotFoundException()

        if candidate_request.status != CandidateRequest.Status.WAITING:
            raise IntegrityBreachException()

        candidate_request.status = status
        candidate_request.save()

        return CandidateRequestSerializer(candidate_request)

    def accept(self, user_id: int):
        return self.set_request_status(user_id, CandidateRequest.Status.ACCEPTED)

    def decline(self, user_id: int):
        return self.set_request_status(user_id, CandidateRequest.Status.DECLINED)
