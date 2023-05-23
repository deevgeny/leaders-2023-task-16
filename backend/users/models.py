from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """Custom user model manager where email is the unique identifier
    for authentication instead of username.
    """

    def create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    """Custom user model."""

    CANDIDATE = "CANDIDATE"
    INTERN = "INTERN"
    CURATOR = "CURATOR"
    STAFF = "STAFF"
    MENTOR = "MENTOR"
    ROLE_CHOICES = [
        (CANDIDATE, "Кандидат"),
        (INTERN, "Стажер"),
        (CURATOR, "Куратор"),
        (STAFF, "Кадровый специалист"),
        (MENTOR, "Наставник")
    ]

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    username = None
    username_validator = None
    objects = CustomUserManager()

    email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(
        verbose_name="Имя",
        max_length=50
    )
    patronymic = models.CharField(
        verbose_name="Отчество",
        max_length=50
    )
    last_name = models.CharField(
        verbose_name="Фамилия",
        max_length=50
    )
    phone = models.CharField(
        verbose_name="Номер телефона",
        max_length=20
    )
    role = models.CharField(
        verbose_name="Роль",
        max_length=9,
        choices=ROLE_CHOICES,
        default=CANDIDATE
    )
    birthday = models.DateField(
        verbose_name="Дата рождения",
        blank=True,
        null=True,
        default=None
    )
    university_name = models.CharField(
        verbose_name="Учебное заведение",
        max_length=50,
        blank=True
    )
    university_year = models.PositiveSmallIntegerField(
        verbose_name="Курс",
        blank=True,
        null=True
    )
    job_experience = models.TextField(
        verbose_name="Опыт",
        blank=True
    )
    skills = models.TextField(
        verbose_name="Навыки",
        blank=True
    )
    departments = models.TextField(
        verbose_name="Предпочитаемые направления стажировки",
        blank=True
    )
