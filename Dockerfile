# Dockerfile

# ---- Base Stage ----
# Use an official Python runtime as a parent image
# Using a specific version is good practice for reproducibility
FROM python:3.12-slim-bullseye

# Set environment variables
# 1. Prevents Python from writing pyc files to disc
# 2. Prevents Python from buffering stdout and stderr
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# ---- Builder Stage ----
# Install system dependencies required for Pillow and psycopg2
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies
# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install -r requirements.txt

# ---- Final Stage ----
# Copy the project code into the container
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Add a healthcheck
HEALTHCHECK CMD curl --fail http://localhost:8000/ || exit 1

# Run entrypoint.sh script
ENTRYPOINT ["/app/entrypoint.sh"]