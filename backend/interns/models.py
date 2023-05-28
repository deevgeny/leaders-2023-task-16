from django.db import models

from staff.models import Organization


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
