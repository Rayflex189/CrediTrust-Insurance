#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Make fresh migrations
python manage.py makemigrations

# Apply any outstanding database migrations
# Use --fake if the column already exists to avoid duplicate migration error
python manage.py migrate axis_app
