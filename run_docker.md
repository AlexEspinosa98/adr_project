# Running PostgreSQL Database Locally with Docker Compose

This guide provides instructions on how to run only the PostgreSQL database locally using Docker Compose. This is useful for local development when you want to manage the database separately from the main application.

## Prerequisites

Make sure you have the following software installed on your machine:

*   [Docker](https://docs.docker.com/get-docker/)
*   [Docker Compose](https://docs.docker.com/compose/install/)

## Step 1: Create `docker-compose.yml` for the Database

Create a file named `docker-compose.yml` in your project root with the following content:

```yaml
version: '3.8'

services:
  db:
    image: postgres:15-alpine
    container_name: adr_db
    environment:
      - POSTGRES_USER=${DB_USER}
      - POSTGRES_PASSWORD=${DB_PASSWORD}
      - POSTGRES_DB=${DB_NAME}
    volumes:
      - postgres_data:/var/lib/postgresql/data/
    ports:
      - "5432:5432"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${DB_USER} -d ${DB_NAME}"]
      interval: 10s
      timeout: 5s
      retries: 5

volumes:
  postgres_data:
```

## Step 2: Configure Environment Variables

Create a `.env` file in the same directory as your `docker-compose.yml` file with the following content. You can change the values as needed.

```
DB_USER=user
DB_PASSWORD=password
DB_NAME=adr
```

## Step 3: Start the Database Service

To start the PostgreSQL database service, navigate to the directory containing your `docker-compose.yml` and `.env` files and run:

```bash
docker-compose up -d
```

*   `up`: Creates and starts the containers.
*   `-d` (or `--detach`): Runs the container in the background.

## Step 4: Verify the Database Service

To check the status of your running database service, use the following command:

```bash
docker-compose ps
```

You should see the `db` service with an `Up` and `healthy` status.

## Step 5: Stop the Database Service

To stop and remove the database container and its associated network and volumes, run:

```bash
docker-compose down
```
