#!/bin/bash

python manage.py collectstatic --noinput

python manage.py migrate

python manage.py demo_users

if [ ! -z $ADMIN_CREDENTIALS_FILE -a -f $ADMIN_CREDENTIALS_FILE ]; then
export $(egrep -v '^#' $ADMIN_CREDENTIALS_FILE | xargs)
python manage.py createsuperuser --noinput || echo
fi

if [ $DEBUG ]; then
python manage.py runserver 0.0.0.0:$BACKEND_PORT $@
else
gunicorn config.wsgi:application -b $BACKEND_PORT $@
fi
