#!/bin/bash

# Exit on error
set -o errexit

echo "Running database migrations..."
python manage.py migrate --no-input

echo "Creating superuser if it doesn't exist..."
python manage.py shell << EOF
from django.contrib.auth import get_user_model;
User = get_user_model();
if not User.objects.filter(username='Paul').exists():
    User.objects.create_superuser('Paul', 'admin@example.com', 'Me12sleep');
    print('Superuser "Paul" created successfully!');
else:
    print('Superuser "Paul" already exists');
EOF

echo "Collecting static files..."
python manage.py collectstatic --no-input

echo "Starting Gunicorn..."
exec gunicorn Axis.wsgi:application --bind 0.0.0.0:8080
