# ADR Project API

This repository contains the backend API for the ADR Project, built with FastAPI.

## Features

- User registration and authentication with API tokens.
- Image uploads for user signatures.
- Dockerized environment for development and production.
- CI/CD pipeline for automated testing and deployment.

## Project Structure

The project follows a modular architecture with a clear separation of concerns:

- `common/`: Shared code for all modules, including domain base classes, infrastructure services, etc.
- `modules/`: Business logic modules (e.g., `auth`). Each module is self-contained with its own domain, application, and infrastructure layers.
- `main.py`: The FastAPI application entry point.
- `Dockerfile`: Defines the Docker image for the application.
- `docker-compose.yml`: Orchestrates the application, database, and migrations.
- `.github/workflows/ci.yml`: GitHub Actions workflow for CI/CD.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Local Development Setup

1.  **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd adr_project
    ```

2.  **Create an environment file:**

    Create a `.env` file by copying the example file:

    ```bash
    cp .env.example .env
    ```

    Update the `.env` file with your desired database credentials.

3.  **Build and run the application:**

    ```bash
    docker-compose up --build
    ```

    This command will:
    - Build the Docker image for the backend application.
    - Start the PostgreSQL database container.
    - Run database migrations.
    - Start the FastAPI backend service.

4.  **Access the API:**

    The API will be available at `http://localhost:8000`.
    You can access the interactive API documentation (Swagger UI) at `http://localhost:8000/docs`.

## Database Migrations

This project uses Alembic to manage database migrations.

### Generating Migrations

When you make changes to the SQLAlchemy models (e.g., in `common/infrastructure/database/models/`), you need to generate a new migration script.

1.  **Ensure your database container is running:**
    ```bash
    docker-compose up -d db
    ```

2.  **Generate the migration script:**
    ```bash
    docker-compose run --rm migration sh -c "alembic revision --autogenerate -m 'Your migration message'"
    ```
    Replace `'Your migration message'` with a short, descriptive message about the changes you made. This will create a new file in the `migrations/versions` directory.

### Applying Migrations

To apply pending migrations to the database, run the following command:

```bash
docker-compose up --build migration
```

This command will start the `migration` service, which is configured to run `alembic upgrade head`. This will apply all migrations that have not yet been applied to the database. The `--build` flag is recommended to ensure the container has the latest code.

The application is configured to run migrations automatically when you run `docker-compose up --build`. However, you can run the migration service independently if you need to.

## Deployment

This section provides a step-by-step guide for deploying the application to a production server.

### Server Setup

1.  **Provision a server:**

    Provision a new server with a public IP address from your preferred cloud provider (e.g., AWS, Google Cloud, DigitalOcean).

2.  **Install Docker and Docker Compose:**

    SSH into your server and install Docker and Docker Compose by following the official documentation.

3.  **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd adr_project
    ```

### Deployment Steps

1.  **Configure environment variables:**

    Create a `.env` file on the server with your production database credentials and any other required environment variables.

2.  **Pull the latest Docker image:**

    If you are using the CI/CD pipeline, the latest Docker image will be pushed to your container registry. Pull the image on your server:

    ```bash
    docker pull <your-docker-hub-username>/adr-backend:latest
    ```

3.  **Run the application:**

    Start the application using Docker Compose:

    ```bash
    docker-compose -f docker-compose.prod.yml up -d
    ```

    *Note: You might want to create a separate `docker-compose.prod.yml` for production that does not mount the source code as a volume.*

## CI/CD Pipeline

The project includes a GitHub Actions workflow defined in `.github/workflows/ci.yml`.

### Workflow

- **Trigger:** The workflow is triggered on every push or pull request to the `main` branch.
- **Jobs:**
    - `build-and-test`: Installs dependencies, runs linters, and executes tests.
    - `build-and-push-docker`: Builds the Docker image and pushes it to Docker Hub (only on pushes to `main`).

### Setup

1.  **Secrets:**

    You need to configure the following secrets in your GitHub repository settings:
    - `DOCKER_HUB_USERNAME`: Your Docker Hub username.
    - `DOCKER_HUB_ACCESS_TOKEN`: Your Docker Hub access token.

2.  **Customization:**

    - **Linting and Testing:** Update the `Run linters` and `Run tests` steps in the `ci.yml` file with your project's specific commands.
    - **Docker Hub:** Change the `tags` in the `build-and-push` step to match your Docker Hub repository.

## API Usage

### Authentication

- Register a new user by sending a `POST` request to `/api/v1/auth/register_extensionist`.
- The response will contain an `api_token`.
- Include this token in the `X-API-TOKEN` header for all authenticated requests.

### Endpoints

- `POST /api/v1/auth/register_extensionist`: Register a new user.
- `PUT /api/v1/auth/extensionist`: Update user information.
- `POST /api/v1/auth/user/signing-image`: Upload a signing image for the user.

For detailed information about the API endpoints and their parameters, please refer to the interactive documentation at `/docs`.
