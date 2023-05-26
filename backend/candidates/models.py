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
    departments = models.TextField(verbose_name="Направления стажировки")
    internship_source = models.TextField(verbose_name="Откуда узнали о стажировке")
    schedule = models.PositiveIntegerField(verbose_name="График работы (кол-во часов)")
    status = models.CharField(
        verbose_name="Статус",
        max_length=16,
        choices=Status.choices,
        default=Status.WAITING,
    )

    class Meta:
        verbose_name = "Заявка кандидата"
        verbose_name_plural = "Заявки кандидатов"
