# Лидеры цифровой трансформации 2023 задача 16

![Tests](https://github.com/deevgeny/leaders-2023-task-16/actions/workflows/tests_workflow.yaml/badge.svg)
![Build](https://github.com/deevgeny/leaders-2023-task-16/actions/workflows/build_workflow.yaml/badge.svg)

Интерактивная платформа-сообщество для стажеров и участников молодежных карьерных проектов

## Установка и запуск
Убедитесь, что у вас установлен [Docker](https://hub.docker.com/).
Далее склонируйте данный репозиторий:
```shell
git clone https://github.com/deevgeny/leaders-2023-task-16
```

Необходимо создать `.env` файл в директории репозитория. Пример файла:
```text
# Postgres settings
POSTGRES_DB=leaders_2023
POSTGRES_USER=user
POSTGRES_PASSWORD=qwerty12

# Backend settings
BACKEND_PORT=8000
DB_ENGINE=django.db.backends.postgresql
DB_HOST=database
DB_PORT=5432
SECRET_KEY='*&nmen=#x6hb$y&gkmvf!a-00p*2q+$6r=3h&0282=vswr8pe@'
ALLOWED_HOSTS=127.0.0.1 localhost backend
CSRF_TRUSTED_ORIGINS=https://example.com
CORS_ALLOWED_ORIGINS=http://localhost:8000
```

Также можно создать файл `admin_credentials` для автоматического создания
аккаунта администратора. Пример файла:
```text
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_PASSWORD=qwerty12
DJANGO_SUPERUSER_FIRST_NAME=Ivan
DJANGO_SUPERUSER_LAST_NAME=Ivanov
DJANGO_SUPERUSER_SURNAME=Ivanovich
```

Для запуска бэкенда воспользуйтесь следующей командой:
```shell
docker compose up backend -d
```

Для остановки сервиса введите следующую команду:
```shell
docker compose down
```
