from candidates.models import CandidateRequest
from candidates.serializers import (
    CandidateRequestSerializer,
    VerboseCandidateRequestSerializer,
)
from core.exceptions import (
    AlreadyExistsException,
    IntegrityBreachException,
    NotFoundException,
)
from users.models import User


class CandidatesService:
    def create(self, user_id: int) -> CandidateRequestSerializer:
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise NotFoundException()

        if hasattr(user, "candidate_request"):
            raise AlreadyExistsException()

        candidate_request = CandidateRequest.objects.create(
            user=user,
            score_percentage=100,  # TODO: Необходимо продумать как будут устроены тесты
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
    ) -> list[VerboseCandidateRequestSerializer]:
        start, end = page * size, (page + 1) * size

        # TODO: Добавить сортировку по рекоммендованным кандидатам
        queryset = CandidateRequest.objects.filter(
            status=CandidateRequest.Status.WAITING
        ).order_by("pk")

        return list(map(VerboseCandidateRequestSerializer, queryset[start:end]))

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
