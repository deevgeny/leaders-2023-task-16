from django.db import models


class Organization(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    name = models.CharField(max_length=32)
    description = models.TextField()
    address = models.CharField(max_length=60)

    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"
