from datetime import date
from random import choice, choices, randint

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError

from candidates.models import CandidateRequest
from users.models import UserInfo

User = get_user_model()

# Users for UI demonstration
demo_users = [
    {
        "email": "candidate@mail.ru",
        "password": "123456",
        "role": "CANDIDATE",
        "first_name": "Ирина",
        "surname": "Сергеевна",
        "last_name": "Воробьева",
        "phone": "+79990001122",
    },
    {
        "email": "intern@mail.ru",
        "password": "123456",
        "role": "INTERN",
        "first_name": "Борис",
        "surname": "Петрович",
        "last_name": "Ким",
        "phone": "+79991112233",
    },
    {
        "email": "mentor@mail.ru",
        "password": "123456",
        "role": "MENTOR",
        "first_name": "Сергей",
        "surname": "Иванович",
        "last_name": "Аршинов",
        "phone": "+79992223344",
    },
    {
        "email": "curator@mail.ru",
        "password": "123456",
        "role": "CURATOR",
        "first_name": "Елена",
        "surname": "Егоровна",
        "last_name": "Орлова",
        "phone": "+79993334455",
    },
    {
        "email": "staff@mail.ru",
        "password": "123456",
        "role": "STAFF",
        "first_name": "Петр",
        "surname": "Александрович",
        "last_name": "Быстров",
        "phone": "+79994445566",
    },
]

# Users to fill database
years = [2000, 1999, 1998, 1997]
mo = [i for i in range(1, 13)]
d = [i for i in range(1, 25)]
user_data = {
    "email": "candidate_{}@mail.ru",
    "password": "123456",
    "role": "CANDIDATE",
    "first_name": "Имя",
    "surname": "Фамилия",
    "last_name": "Отчество",
    "phone": "+7800{}",
    "gender": ["MALE", "FEMALE"],
    "city": "Москва",
    "district": [
        "ЦАО",
        "САО",
        "СВАО",
        "ЮВАО",
        "ЮАО",
        "ЮЗАО",
        "ЗАО",
        "СЗАО",
        "ЗелАО",
        "ТиНАО",
    ],
    "education_institution": [
        "Учебное заведение №1",
        "Учебное заведение №2",
        "Учебное заведение №3",
    ],
    "education_city": "Москва",
    "faculty": "Факультет",
    "speciality": [
        "Специальность 1",
        "Специальность 2",
        "Специальность 3",
        "Специальность 4",
    ],
    "graduation_year": [2024, 2025, 2023, 2026, 2027],
    "education_level": ["Специалист", "Магистр", "Бакалавр"],
    "has_job_experience": [True, False],
    "has_volunteer_experience": [True, False],
    "job_experience": [
        "Описание опыта 1",
        "Описание опыта 2",
        "Описание опыта 3",
        "Описание опыта 4",
    ],
    "citizenship": ["РФ", "Другое 1", "Другое 2"],
    "photo_url": "https://robohash.org/{}",
}

# Candidate requests to fill database
user_requests = {
    "departments": ["HR", "IT", "МГ", "КГС", "ПП", "ГЭ", "СГ"],
    "internship_source": ["Интернет", "Реклама", "Знакомые", "Другое"],
    "chedule": [20, 40],
    "status": ["WAITING", "ACCEPTED", "DECLINED"],
}


class Command(BaseCommand):
    """Custom command to create demo users."""

    def handle(self, *args, **options):
        # Create UI demo users
        for user in demo_users:
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


        # Skip candidates creation  
        if User.objects.count() > 100:
            return

        # Create candidates
        for i in range(1, 101):
            try:
                user = User.objects.create_user(
                    email=user_data["email"].format(i),
                    password=user_data["password"],
                    role=user_data["role"],
                    first_name=user_data["first_name"],
                    surname=user_data["surname"],
                    last_name=user_data["last_name"],
                    phone=user_data["phone"].format(5550000 + i),
                )
                self.stdout.write(self.style.SUCCESS("SUCCESS: Db data user created."))
                # Create user info
                UserInfo.objects.create(
                    user=user,
                    birthdate=date(choice(years), choice(mo), choice(d)),
                    gender=choice(user_data["gender"]),
                    city=user_data["city"],
                    district=choice(user_data["district"]),
                    education_institution=choice(user_data["education_institution"]),
                    education_city=user_data["education_city"],
                    faculty=choice(user_data["faculty"]),
                    speciality=choice(user_data["speciality"]),
                    graduation_year=choice(user_data["graduation_year"]),
                    education_level=choice(user_data["education_level"]),
                    has_job_experience=choice(user_data["has_job_experience"]),
                    has_volunteer_experience=choice(user_data["has_volunteer_experience"]),
                    job_experience=choice(user_data["job_experience"]),
                    citizenship=choice(user_data["citizenship"]),
                    photo_url=user_data["photo_url"].format(i),
                )
                self.stdout.write(self.style.SUCCESS("SUCCESS: Db data info created."))
                # Create candidate request
                CandidateRequest.objects.create(
                    user=user,
                    departments=choice(user_requests["departments"]),
                    internship_source=choice(user_requests["internship_source"]),
                    schedule=choice(user_requests["chedule"]),
                    status=choice(user_requests["status"]),
                )
                self.stdout.write(
                    self.style.SUCCESS("SUCCESS: Db data request created.")
                )

            except IntegrityError:
                self.stdout.write(
                    self.style.ERROR("ERROR: Db data user already exists.")
                )
            # except BaseException:
            #    self.stdout.write(
            #        self.style.ERROR("ERROR: Unexpected error.")
            #    )
