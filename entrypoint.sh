#!/bin/bash

# Exit on error
set -o errexit

echo "Running database migrations..."
python manage.py migrate --no-input

echo "Collecting static files..."
python manage.py collectstatic --no-input

echo "Starting Gunicorn..."
exec gunicorn Axis.wsgi:application --bind 0.0.0.0:8080
