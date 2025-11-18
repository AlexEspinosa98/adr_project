#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")"

echo "===> Apagando contenedores del proyecto (si existen)"
docker compose down --remove-orphans || docker-compose down --remove-orphans || true

echo "===> Matando contenedor suelto 'adr_backend_container' (si existe, usa el puerto 8000)"
if docker ps -a --format '{{.Names}}' | grep -qx 'adr_backend_container'; then
  docker rm -f adr_backend_container || true
fi

echo "===> Reconstruyendo imagen del backend"
if docker compose version &>/dev/null; then
  docker compose build backend
else
  docker-compose build backend
fi

echo "===> Levantando base de datos, migraciones y backend en segundo plano"
if docker compose version &>/dev/null; then
  docker compose up -d
else
  docker-compose up -d
fi

echo "===> Estado actual de los servicios:"
if docker compose version &>/dev/null; then
  docker compose ps
else
  docker-compose ps
fi
