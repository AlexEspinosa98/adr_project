#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")"

if command -v docker-compose &>/dev/null; then
  DC="docker-compose"
else
  DC="docker compose"
fi

CONTAINER_NAME="adr_db"

if ! docker ps --format '{{.Names}}' | grep -qx "$CONTAINER_NAME"; then
  echo "[DB] El contenedor $CONTAINER_NAME no está corriendo"
  docker ps --format 'table {{.Names}}\t{{.Status}}'
  exit 1
fi

STATUS=$(docker inspect -f '{{.State.Health.Status}}' "$CONTAINER_NAME" 2>/dev/null || echo "unknown")

echo "[DB] Estado del contenedor: $STATUS"

if [[ "$STATUS" != "healthy" ]]; then
  echo "[DB] La base de datos no está healthy (estado=$STATUS)"
  exit 1
fi

DB_USER=${DB_USER:-user}
DB_NAME=${DB_NAME:-adr}

echo "[DB] Probando conexión con pg_isready..."
docker exec "$CONTAINER_NAME" pg_isready -U "$DB_USER" -d "$DB_NAME"

if command -v psql &>/dev/null; then
  echo "[DB] Probando conexión desde el host con psql..."
  PGPASSWORD="${DB_PASSWORD:-password}" psql -h 127.0.0.1 -p 5432 -U "$DB_USER" -d "$DB_NAME" -c 'SELECT 1;' >/dev/null && \
    echo "[DB] Conexión exitosa desde el host" || \
    echo "[DB] NO se pudo conectar desde el host"
else
  echo "[DB] psql no está instalado en el host, solo se verificó desde el contenedor"
fi

echo "[DB] OK"
