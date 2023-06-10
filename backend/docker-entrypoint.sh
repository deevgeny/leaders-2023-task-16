#!/bin/bash

if [ $CELERY ]; then
    if [ $DEBUG ]; then
        celery -A config worker -l DEBUG
        exit 0
    else
        celery -A config worker -l INFO
        exit 0
fi

python manage.py collectstatic --noinput

python manage.py migrate

if [ ! -z $ADMIN_CREDENTIALS_FILE -a -f $ADMIN_CREDENTIALS_FILE ]; then
export $(egrep -v '^#' $ADMIN_CREDENTIALS_FILE | xargs)
python manage.py createsuperuser --noinput || echo
fi

# Skip database fill
# python manage.py demo_users

if [ $DEBUG ]; then
python manage.py runserver 0.0.0.0:$BACKEND_PORT $@
else
gunicorn config.wsgi:application -b $BACKEND_PORT $@
fi
