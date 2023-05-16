#!/bin/bash

python manage.py collectstatic --noinput

python manage.py migrate

if [ $DEBUG ]; then
python manage.py runserver 0.0.0.0:$BACKEND_PORT $@
else
gunicorn config.wsgi:application -b $BACKEND_PORT $@
fi
