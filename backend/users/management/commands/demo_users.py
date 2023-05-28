from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError

User = get_user_model()

users = [
    {
        "email": "candidate@mail.ru",
        "password": "123456",
        "role": "CANDIDATE",
        "first_name": "Иван",
        "surname": "Иванович",
        "last_name": "Иванов",
        "phone": "+79990001122",
    },
    {
        "email": "intern@mail.ru",
        "password": "123456",
        "role": "INTERN",
        "first_name": "Иван",
        "surname": "Иванович",
        "last_name": "Иванов",
        "phone": "+79991112233",
    },
    {
        "email": "mentor@mail.ru",
        "password": "123456",
        "role": "MENTOR",
        "first_name": "Иван",
        "surname": "Иванович",
        "last_name": "Иванов",
        "phone": "+79992223344",
    },
    {
        "email": "curator@mail.ru",
        "password": "123456",
        "role": "CURATOR",
        "first_name": "Иван",
        "surname": "Иванович",
        "last_name": "Иванов",
        "phone": "+79993334455",
    },
    {
        "email": "staff@mail.ru",
        "password": "123456",
        "role": "STAFF",
        "first_name": "Иван",
        "surname": "Иванович",
        "last_name": "Иванов",
        "phone": "+79994445566",
    },
]


class Command(BaseCommand):
    """Custom command to create demo users."""

    def handle(self, *args, **options):
        for user in users:
            try:
                User.objects.create_user(
                    email=user["email"],
                    password=user["password"],
                    role=user["role"],
                    first_name=user["first_name"],
                    surname=user["surname"],
                    last_name=user["last_name"],
                    phone=user["phone"],
                )
                self.stdout.write(self.style.SUCCESS("SUCCESS: Demo user created."))
            except IntegrityError:
                self.stdout.write(self.style.ERROR("ERROR: Demo user already exists."))
