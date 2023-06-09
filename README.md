# Лидеры цифровой трансформации 2023 задача 16

[![MIT License](https://img.shields.io/github/license/deevgeny/leaders-2023-task-16)](https://github.com/deevgeny/leaders-2023-task-16/blob/main/LICENSE)
![Tests](https://github.com/deevgeny/leaders-2023-task-16/actions/workflows/tests_workflow.yaml/badge.svg)
![Build](https://github.com/deevgeny/leaders-2023-task-16/actions/workflows/build_workflow.yaml/badge.svg)
![Deploy](https://github.com/deevgeny/leaders-2023-task-16/actions/workflows/deploy_workflow.yaml/badge.svg)

Интерактивная платформа-сообщество для стажеров и участников молодежных карьерных проектов

## Стек

* Бэкэнд
    * Python 3.10
    * Django 4.2.1
    * Django REST Framework 3.14.0
    * Postgresql 15

* Фронтэнд
    * React 18.2.0
    * Material UI 5
    * Axios 1.4.0
    * Vite 4.3.2

* Инфраструктура
    * Docker 24.0
    * Docker compose 2.17.3
    * Nginx 1.21.3


## Установка и запуск

Предусмотрено три варианта запуска проекта:
1. Локально со сборкой докер образов без прокси сервера (docker-compose.yaml).
2. Локально со сборкой образов с прокси сервером (docker-compose.deploy.yaml).
3. Локально/на сервере без сборки образов с прокси сервером (docker-compose.server.yaml).

Убедитесь, что у вас установлен [Docker](https://hub.docker.com/).\
Так же потребуется [Pipenv](https://docs.pipenv.org/install/).\
\
Далее склонируйте данный репозиторий:
```sh
# Клонировать
git clone https://github.com/deevgeny/leaders-2023-task-16

# Перейти в директорию бэкэнда
cd backend
```

Cоздать `.env` файл в директории бэкэнда.\
Пример файла:
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
аккаунта администратора.\
Пример файла:
```text
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_PASSWORD=qwerty12
DJANGO_SUPERUSER_FIRST_NAME=Ivan
DJANGO_SUPERUSER_LAST_NAME=Ivanov
DJANGO_SUPERUSER_SURNAME=Ivanovich
```
Создайте виртуальное окружение и установите зависимости
```sh
# Создать и активировать виртуальное окружение
pipenv shell

# Установить зависимости
pipenv install
```
Для запуска проекта, вернитесь в корневую директорию репозитория и воспользуйтесь следующей командой:
```sh
# Вернуться в корневую директорию проекта
cd ..

# Первый вариант запуск
docker compose up -d

# Второй вариант запуск
docker compose up -f docker-compose.deploy.yaml up -d

# Третий вариант запуска
docker compose up -f docker-compose.server.yaml up -d
```

Для остановки введите следующую команду:
```sh
# Первый вариант
docker compose down

# Второй вариант
docker compose up -f docker-compose.deploy.yaml down

# Третий вариант
docker compose up -f docker-compose.server.yaml down
```

После запуска будут доступны следующие ресурсы:

* Первый вариант:
    * [http://localhost](http://localhost) - главная страница 
    * [http://localhost/admin/](http://localhost/admin/) - админ панель 
    * [http://localhost/swagger/](http://localhost/swagger/) - API документация 
    * [http://localhost:8080](http://localhost:8080) - веб интерфейс базы данных
* Второй и третий вариант:
    * [http://localhost](http://localhost) - главная страница 
    * [http://localhost/admin/](http://localhost/admin/) - админ панель 
    * [http://localhost/api/v1/swagger/](http://localhost/api/v1/swagger/) - API документация 
    * [http://localhost/adminer/](http://localhost/adminer/) - веб интерфейс базы данных

