from django.db import models

from users.models import User


class CandidateRequest(models.Model):
    class Status(models.TextChoices):
        WAITING = "WAITING", "Ожидает рассмотрения"
        ACCEPTED = "ACCEPTED", "Принята"
        DECLINED = "DECLINED", "Отклонена"

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="candidate_request",
    )
    score_percentage = models.PositiveSmallIntegerField(
        verbose_name="Процент выполнения теста"
    )
    status = models.CharField(
        verbose_name="Статус",
        max_length=16,
        choices=Status.choices,
        default=Status.WAITING,
    )

    class Meta:
        verbose_name = "Заявка кандидата"
        verbose_name_plural = "Заявки кандидатов"
