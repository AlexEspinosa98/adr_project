# ADR Project

This document provides instructions on how to set up and run this project using Docker, and how to manage database migrations using Alembic.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Make sure you have the following software installed on your machine:

*   [Docker](https://docs.docker.com/get-docker/)
*   [Docker Compose](https://docs.docker.com/compose/install/)

### Running the Application with Docker

The application is containerized using Docker and can be easily managed with Docker Compose. This is the recommended way to run the application for development.

**Step 1: Configure Environment Variables**

The application uses a `.env` file to manage environment-specific variables, such as database credentials. A `.env.example` file is provided in the root of the project.

Create a `.env` file by copying the example file. The default values are suitable for the local Docker environment.

```bash
cp .env.example .env
```

The `.env` file should look like this:

```
DB_USER=user
DB_PASSWORD=password
DB_NAME=adr
DB_HOST=db
```

**Step 2: Build and Start the Services**

Once the `.env` file is configured, you can build and start all the services (backend application and database) using a single command:

```bash
docker-compose up -d --build
```

*   `up`: Creates and starts the containers.
*   `-d` (or `--detach`): Runs the containers in the background.
*   `--build`: Forces a rebuild of the Docker images before starting the containers. This is useful when you have made changes to the code or dependencies.

This command will:
1.  Build the Docker images for the application.
2.  Start a PostgreSQL database container.
3.  Wait for the database to be ready.
4.  Run database migrations automatically.
5.  Start the backend application container.

**Step 3: Verify the Services**

To check the status of your running services, use the following command:

```bash
docker-compose ps
```

You should see the `backend` and `db` services with a `Up` or `healthy` status.

The backend application will be accessible at [http://localhost:8000](http://localhost:8000).

**Step 4: View Application Logs**

To view the real-time logs from the running services, which is useful for debugging, run:

```bash
docker-compose logs -f
```

To view the logs of a specific service, add the service name at the end, for example: `docker-compose logs -f backend`.

**Step 5: Stop the Application**

To stop and remove all the containers, networks, and volumes created by `docker-compose up`, run:

```bash
docker-compose down
```

## Database Migrations (Alembic)

Database schema migrations are managed with Alembic. A custom command-line interface is provided in `migrations_service/cli.py` to simplify the process.

While migrations are run automatically when you start the application with Docker, you may need to create or manage them manually during development.

### Creating a New Migration

After you have made changes to your SQLAlchemy models (e.g., in `common/infrastructure/database/models/`), you need to generate a new migration script.

To do this, run the following command from the root of the project:

```bash
python migrations_service/cli.py make "Your descriptive migration message"
```

This will create a new migration file in the `migrations/versions/` directory.

### Applying Migrations

To apply all pending migrations to the database, run:

```bash
python migrations_service/cli.py upgrade
```

This command applies migrations up to the latest version (`head`).

### Reverting Migrations

To revert the last applied migration, run:

```bash
python migrations_service/cli.py downgrade
```

You can also revert to a specific migration version by providing its revision ID.
