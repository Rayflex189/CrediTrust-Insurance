# Use official slim Python 3.12 image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_ROOT_USER_ACTION=ignore

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY Axis/requirements.txt .
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy the full Django project
COPY Axis/ .

# Collect static files at build time
RUN python manage.py collectstatic --no-input

# Copy entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Expose the port Django will run on
EXPOSE 8000

# Set entrypoint
ENTRYPOINT ["/entrypoint.sh"]

# Start Gunicorn server
CMD ["gunicorn", "Axis.wsgi:application", "--bind", "0.0.0.0:8000"]
