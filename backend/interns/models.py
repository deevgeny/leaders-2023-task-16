from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth import get_user_model

from staff.models import Organization

User = get_user_model()


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
        max_length=16, choices=Status.choices, default=Status.WAITING, db_index=True
    )


class InternIntro(models.Model):
    """Intern INTRO stage data model."""

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="intro"
    )
    url = models.URLField(
        verbose_name="Ссылка для перехода на стороннюю платформу"
    )
    progress = models.PositiveSmallIntegerField(
        verbose_name="Прогресс карьерной школы",
        default=0,
        validators=[MaxValueValidator(limit_value=100)]
    )

    class Meta:
        verbose_name = "Карьерная школа"
        verbose_name_plural = "Карьерная школа"
