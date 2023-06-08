from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from staff.models import Organization


class UserManager(BaseUserManager):
    def create_user(
        self,
        email: str,
        password: str,
        first_name: str,
        last_name: str,
        surname: str,
        **extra_fields
    ) -> "User":
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            surname=surname,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(
        self,
        email: str,
        password: str,
        first_name: str,
        last_name: str,
        surname: str,
        **extra_fields
    ):
        user = self.create_user(
            email, password, first_name, last_name, surname, **extra_fields
        )
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    class Role(models.TextChoices):
        CANDIDATE = "CANDIDATE", "Кандидат"
        INTERN = "INTERN", "Стажер"
        CURATOR = "CURATOR", "Куратор"
        STAFF = "STAFF", "Кадровый специалист"
        MENTOR = "MENTOR", "Наставник"

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "surname"]

    objects = UserManager()

    email = models.EmailField("E-Mail", unique=True)
    role = models.CharField(
        verbose_name="Роль",
        max_length=16,
        choices=Role.choices,
        default=Role.CANDIDATE,
        db_index=True,
    )
    first_name = models.CharField(verbose_name="Имя", max_length=50)
    last_name = models.CharField(verbose_name="Фамилия", max_length=50)
    surname = models.CharField(verbose_name="Отчество", max_length=50)
    phone = models.CharField(verbose_name="Номер телефона", max_length=20,
                             blank=True)

    organization = models.ForeignKey(
        Organization, on_delete=models.RESTRICT, verbose_name="Организация",
        null=True
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    @property
    def is_staff(self):
        return self.is_superuser

    @property
    def is_active(self):
        return True


class UserInfo(models.Model):
    class Gender(models.TextChoices):
        MALE = "MALE", "Мужской"
        FEMALE = "FEMALE", "Женский"

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="info"
    )
    birthdate = models.DateField(
        verbose_name="Дата рождения",
        blank=True,
        null=True,
        db_index=True)
    gender = models.CharField(
        verbose_name="Пол",
        max_length=6,
        choices=Gender.choices,
        blank=True,
        null=True
    )
    city = models.CharField(
        verbose_name="Город проживания",
        max_length=60,
        blank=True
    )
    district = models.CharField(
        verbose_name="Район проживания",
        max_length=60,
        blank=True
    )
    education_institution = models.CharField(
        verbose_name="Учебное заведение",
        max_length=60,
        blank=True
    )
    education_city = models.CharField(
        verbose_name="Город обучения",
        max_length=60,
        blank=True
    )
    faculty = models.CharField(
        verbose_name="Факультет",
        max_length=60,
        blank=True
    )
    speciality = models.CharField(
        verbose_name="Специальность",
        max_length=60,
        blank=True
    )
    graduation_year = models.PositiveIntegerField(
        verbose_name="Год выпуска",
        null=True
    )
    education_level = models.CharField(
        verbose_name="Уровень образования",
        max_length=60,
        blank=True
    )
    has_job_experience = models.BooleanField(
        verbose_name="Имеется опыт работы",
        null=True
    )
    has_volunteer_experience = models.BooleanField(
        verbose_name="Имеется опыт волонтерства",
        null=True
    )
    job_experience = models.TextField(
        verbose_name="Опыт работы",
        blank=True
    )
    citizenship = models.CharField(
        verbose_name="Гражданство",
        blank=True,
        max_length=50
    )
    photo_url = models.URLField(
        verbose_name="Прямая ссылка на фотографию",
        null=True
    )
    vk_id = models.CharField(
        verbose_name="VK id",
        max_length=60,
        blank=True
    )
    telegram_id = models.CharField(
        verbose_name="Telegram id",
        max_length=60,
        blank=True
    )

    class Meta:
        verbose_name = "Информация о пользователе"


class UserState(models.Model):
    """Abstract user state model."""

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="state"
    )

    class Meta:
        abstract = True


class InternshipState(UserState):
    """Internship state selection model."""

    class Stage(models.TextChoices):
        REQUEST = "REQUEST", "Заявка"
        SCHOOL = "SCHOOL", "Карьерная школа"
        TEST = "TEST", "Тестирование"
        CASE = "CASE", "Кейс чемпионат"
        CHOICE = "CHOICE", "Выбор места стажировки"
        WORK = "WORK", "Работа на месте стажировки"

    stage = models.CharField(
        verbose_name="Этап отбора",
        max_length=16,
        choices=Stage.choices,
        default=Stage.REQUEST
    )
    request_status = models.CharField(
        verbose_name="Заявка",
        max_length=16,
        default=""
    )
    school_status = models.CharField(
        verbose_name="Карьерная школа",
        max_length=16,
        default="",
    )
    test_status = models.CharField(
        verbose_name="Тестирование",
        max_length=16,
        default=""
    )
    case_status = models.CharField(
        verbose_name="Кейс чемпионат",
        max_length=16,
        default=""
    )
    choice_status = models.CharField(
        verbose_name="Выбор места стажировки",
        max_length=16,
        default=""
    )
    work_status = models.CharField(
        verbose_name="Работа на месте стажировки",
        max_length=16,
        default=""
    )

    class Meta:
        verbose_name = "Отбор на стажировку"
