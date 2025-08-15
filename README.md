# Django Newspaper App (Dockerized)

This is a classic newspaper application built with Django. This version has been fully containerized using Docker and Docker Compose, providing a clean, reproducible, and robust environment for development and deployment.

The application features user authentication (sign up, log in, log out), article creation, editing, and deletion, and a comment system.

![Newspaper App Screenshot](https://github.com/bruceminanga/Djangonewspaperapp/blob/main/screenshots/home.png)

## Core Technologies

- **Backend:** Django 5.0
- **Database:** Sqlite3
- **Web Server:** Gunicorn
- **Containerization:** Docker, Docker Compose

## Features

- **Complete Docker Environment:** One command to set up the entire stack, including the Django app and PostgreSQL database.
- **Production-Ready Stack:** Uses Gunicorn as the application server, a standard for production Django deployments.
- **Environment-Based Configuration:** Securely manages settings like `SECRET_KEY` and database credentials using environment variables (via a `.env` file).
- **Persistent Database:** Uses a Docker volume to ensure your database data persists across container restarts.
- **Live Reloading:** The development server is configured for live code reloading, so changes you make on your local machine are instantly reflected in the container.

---

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/) (Usually included with Docker Desktop)

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/bruceminanga/Djangonewspaperapp.git
    cd Djangonewspaperapp
    ```

2.  **Create the Environment File:**
    The application uses a `.env` file to manage secrets and environment-specific settings. You can create one by copying the example file:

    ```bash
    cp .env.example .env
    ```

    _Note: The default values in `.env.example` are suitable for local development. You should generate a new `SECRET_KEY` for any real deployment._

3.  **Build and Run the Docker Containers:**
    This single command will build the Django image, pull the PostgreSQL image, and start all services in the background.

    ```bash
    docker compose up --build -d
    ```

    The initial build might take a few minutes. Subsequent builds will be much faster thanks to Docker's caching.

4.  **Apply Database Migrations:**
    The `entrypoint.sh` script automatically applies migrations when the container starts. To check logs and ensure this completed successfully, you can run:

    ```bash
    docker compose logs -f web
    ```

    You should see output indicating that migrations are being applied and the Gunicorn server is starting. Press `Ctrl+C` to exit the logs.

5.  **Create a Superuser:**
    To access the Django admin panel, you'll need to create a superuser account.
    ```bash
    docker compose exec web python manage.py createsuperuser
    ```
    Follow the prompts to enter a username, email, and password.

**You're all set!** The application should now be running.

- **Website:** [http://localhost:8000](http://localhost:8000)
- **Admin Panel:** [http://localhost:8000/admin/](http://localhost:8000/admin/)

---

## Development Workflow

This setup is designed for an efficient development workflow.

### Running Management Commands

To run any `manage.py` command, use `docker-compose exec web`:

```bash
# Example: Create new migrations after changing your models
docker compose exec web python manage.py makemigrations

# Example: Open a Django shell
docker compose exec web python manage.py shell
```
