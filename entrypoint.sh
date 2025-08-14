#!/bin/sh

# Wait for the database to be ready
# We use a small loop and netcat to check if the PostgreSQL port is open
echo "Waiting for postgres..."
while ! nc -z db 5432; do
  sleep 0.1
done
echo "PostgreSQL started"

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Collect static files
# --noinput flag is important for non-interactive execution
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Start the Gunicorn server
# It listens on all network interfaces (0.0.0.0) on port 8000
echo "Starting Gunicorn server..."
exec gunicorn config.wsgi:application --bind 0.0.0.0:8000