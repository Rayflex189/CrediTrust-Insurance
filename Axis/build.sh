#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input

# Reset migrations safely
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete

# Make and apply fresh migrations
python manage.py makemigrations --noinput
python manage.py migrate --fake-initial --noinput