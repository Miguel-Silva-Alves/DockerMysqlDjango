#!/bin/bash -x

python manage.py makemigrations
python manage.py migrate --noinput


if [ "$DJANGO_SUPERUSER_USERNAME" ]
then
    python manage.py createsuperuser \
        --noinput \
        --username $DJANGO_SUPERUSER_USERNAME \
        --email $DJANGO_SUPERUSER_EMAIL
fi

python manage.py runserver 0.0.0.0:3000

$@