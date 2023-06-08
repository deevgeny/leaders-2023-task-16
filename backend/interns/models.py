from django.contrib.auth import get_user_model
from django.db import models

from staff.models import Organization

User = get_user_model()


class InternCase(models.Model):
    """Intern case model for CASE stage."""

    class Status(models.TextChoices):
        PASS = "PASS", "Пройден"
        FAIL = "FAIL", "Не пройден"
        WAITING = "WAITING", "Ожидает прохождения"

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="case"
    )
    name = models.CharField(
        verbose_name="Название",
        max_length=128
    )
    description = models.TextField(
        verbose_name="Описание кейс чемпионата",
    )
    solution = models.FileField(
        verbose_name="Решение",
        upload_to="case_solutions/",
        null=True,
        blank=True
    )
    status = models.CharField(
        verbose_name="Результат чемпионата",
        max_length=16,
        choices=Status.choices,
        default=Status.WAITING,
    )

    class Meta:
        verbose_name = "Кейс чемпионат"
        verbose_name_plural = "Кейс чемпионаты"


class InternsRequest(models.Model):
    class Status(models.TextChoices):
        WAITING = "WAITING", "Ожидает рассмотрения"
        ACCEPTED = "ACCEPTED", "Одобрена"
        DECLINED = "DECLINED", "Отклонена"

    organization = models.ForeignKey(
        Organization,
        on_delete=models.RESTRICT,
        related_name="interns_requests",
        verbose_name="Организация",
    )
    name = models.CharField(max_length=50)
    description = models.TextField()
    test = models.TextField()
    status = models.CharField(
        max_length=16,
        choices=Status.choices,
        default=Status.WAITING,
        db_index=True
    )
