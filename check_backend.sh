#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")"

BACKEND_URL="${BACKEND_URL:-http://localhost:8000}"
HEALTH_PATH="${BACKEND_HEALTH_PATH:-/docs}"

# Intentar detectar el contenedor del backend
CONTAINER_NAME=""

if docker compose version &>/dev/null; then
  # Intentar obtener el contenedor del servicio backend vía docker compose
  CONTAINER_NAME=$(docker compose ps -q backend 2>/dev/null || true)
  if [[ -n "$CONTAINER_NAME" ]]; then
    CONTAINER_NAME=$(docker ps --filter "id=$CONTAINER_NAME" --format '{{.Names}}')
  fi
else
  # Fallback: buscar por nombre clásico
  if docker ps --format '{{.Names}}' | grep -qx 'adr_backend'; then
    CONTAINER_NAME="adr_backend"
  elif docker ps --format '{{.Names}}' | grep -qx 'adr_backend_container'; then
    CONTAINER_NAME="adr_backend_container"
  fi
fi

if [[ -z "$CONTAINER_NAME" ]]; then
  echo "[BE] No se encontró contenedor de backend (servicio 'backend')"
  docker ps --format 'table {{.Names}}\t{{.Status}}'
  exit 1
fi

STATUS=$(docker inspect -f '{{.State.Status}}' "$CONTAINER_NAME" 2>/dev/null || echo "unknown")

echo "[BE] Contenedor: $CONTAINER_NAME"
echo "[BE] Estado del contenedor: $STATUS"

if [[ "$STATUS" != "running" ]]; then
  echo "[BE] El backend no está corriendo (estado=$STATUS)"
  exit 1
fi

if ! command -v curl &>/dev/null; then
  echo "[BE] curl no está instalado, no puedo hacer healthcheck HTTP"
  exit 0
fi

URL="$BACKEND_URL$HEALTH_PATH"

echo "[BE] Probando endpoint $URL ..."

set +e
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" "$URL")
CURL_EXIT=$?
set -e

echo "[BE] Código HTTP: $HTTP_CODE (curl exit=$CURL_EXIT)"

if [[ "$CURL_EXIT" -ne 0 ]]; then
  echo "[BE] Falló curl contra $URL"
  exit 1
fi

if [[ "$HTTP_CODE" =~ ^2[0-9]{2}$ || "$HTTP_CODE" == "302" ]]; then
  echo "[BE] Backend responde correctamente"
  exit 0
else
  echo "[BE] Backend respondió con un código inesperado"
  exit 1
fi
