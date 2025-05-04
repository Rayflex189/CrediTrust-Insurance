#!/usr/bin/env bash
# Exit on error
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input

# Safe migration without deleting history
python manage.py makemigrations --noinput
python manage.py migrate --noinput