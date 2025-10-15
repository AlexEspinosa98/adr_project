# Commands Guide

This guide provides a summary of the most important commands for developing, testing, and deploying the ADR Project API.

## Local Development

These commands are used to manage the local development environment with Docker Compose.

### Start the environment

To build the Docker images and start the application, database, and migration services, run:

```bash
docker-compose up --build
```

- `--build`: Forces the build of the Docker images.
- You can add the `-d` flag to run the containers in detached mode (in the background):

  ```bash
  docker-compose up --build -d
  ```

### Stop the environment

To stop and remove the containers, networks, and volumes created by `docker-compose up`, run:

```bash
docker-compose down
```

### View logs

To view the logs from all running services, run:

```bash
docker-compose logs -f
```

- `-f`: Follows the log output.

## Testing and Linting

To run commands such as tests or linters inside the running backend container, use `docker-compose exec`.

### Run tests

Assuming you have `pytest` configured, you can run the test suite with:

```bash
docker-compose exec backend pytest
```

### Run linters

Assuming you are using `ruff`, you can check the code for linting errors with:

```bash
docker-compose exec backend ruff check .
```

### Open a shell

To open an interactive shell inside the backend container, run:

```bash
docker-compose exec backend /bin/sh
```

## API Interaction

You can use `curl` or any API client to interact with the running API.

### Register a new user

This will create a new user and return an `api_token`.

```bash
curl -X POST "http://localhost:8000/api/v1/auth/register_extensionist" -H "Content-Type: application/json" -d '{
  "name": "Test User",
  "email": "test@example.com",
  "phone": "1234567890",
  "type_id": "cc",
  "identification": "123456789",
  "city": "Test City",
  "zone": "Test Zone"
}'
```

### Update user information

Replace `<your_api_token>` with the token you received during registration.

```bash
curl -X PUT "http://localhost:8000/api/v1/auth/extensionist" -H "Content-Type: application/json" -H "X-API-TOKEN: <your_api_token>" -d '{
  "name": "New Name",
  "phone": "0987654321"
}'
```

### Upload a signing image

Replace `<your_api_token>` with your token and `/path/to/your/image.png` with the actual path to an image file.

```bash
curl -X POST "http://localhost:8000/api/v1/auth/user/signing-image" -H "X-API-TOKEN: <your_api_token>" -F "file=@/path/to/your/image.png"
```

## Deployment

For detailed deployment instructions, please refer to the `README.md` file. The main commands for a production environment are:

### Pull the latest image

```bash
docker pull <your-docker-hub-username>/adr-backend:latest
```

### Start the application

```bash
docker-compose -f docker-compose.prod.yml up -d
```

*Note: It is recommended to use a separate `docker-compose.prod.yml` for production.*
