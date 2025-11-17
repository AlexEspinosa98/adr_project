# Docker: comandos útiles para reiniciar y actualizar servicios

Este proyecto usa `docker-compose.yml` para levantar:
- Base de datos Postgres (`adr_db`, puerto 5432)
- Servicio de migraciones (`migration`)
- Backend FastAPI (`adr_backend`, puerto 8000)

## 1. Levantar todo desde cero

```bash
# Apaga y elimina contenedores, redes y huérfanos
docker compose down --remove-orphans

# Reconstruye las imágenes si cambió el código o dependencias
docker compose build

# Levanta todo en segundo plano
docker compose up -d
```

## 2. Reiniciar solo la base de datos

```bash
# Reinicia el contenedor de Postgres
docker compose restart db
```

## 3. Reiniciar solo el backend

```bash
# Reinicia el contenedor del backend
docker compose restart backend
```

## 4. Aplicar cambios de código (backend) sin tocar la base de datos

```bash
# Reconstruye solo el backend
docker compose build backend

# Reinicia backend con la nueva imagen
docker compose up -d backend
```

## 5. Forzar re-creación de todos los contenedores

```bash
# Recrea los contenedores aunque no haya cambios aparentes
docker compose up -d --force-recreate
```

## 6. Ver logs

```bash
# Logs de todos los servicios
docker compose logs -f

# Logs solo de la base de datos
docker compose logs -f db

# Logs solo del backend
docker compose logs -f backend
```

## 7. Estado de los contenedores

```bash
docker compose ps
```

