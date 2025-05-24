#!/bin/bash

# Exit on error
set -o errexit

# Run database migrations
python manage.py migrate

# Create admin user if custom command exists
if python manage.py help | grep -q "create_admin"; then
    python manage.py create_admin
fi

# Run the main container command (Gunicorn)
exec "$@"
