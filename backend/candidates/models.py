from django.core.validators import MaxValueValidator
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
    departments = models.TextField(
        verbose_name="Направления стажировки"
    )
    internship_source = models.TextField(
        verbose_name="Откуда узнали о стажировке"
    )
    schedule = models.PositiveIntegerField(
        verbose_name="График работы (кол-во часов)"
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


class CandidateCareerSchool(models.Model):
    """Candidate career school model for SCHOOL stage."""

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="school"
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


class CandidateTest(models.Model):
    """Candidate test model for TEST stage."""

    class Status(models.TextChoices):
        PASS = "PASS", "Пройден"
        FAIL = "FAIL", "Не пройден"
        WAITING = "WAITING", "Ожидает прохождения"

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="test"
    )
    url = models.URLField(
        verbose_name="Ссылка для перехода на стороннюю платформу"
    )
    status = models.CharField(
        verbose_name="Результат тестирования",
        max_length=16,
        choices=Status.choices,
        default=Status.WAITING,
    )

    class Meta:
        verbose_name = "Тест кандидата"
        verbose_name_plural = "Тесты кандидатов"
