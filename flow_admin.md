# Flujo Admin para Exploración de Encuestas

Esta historia de usuario describe cómo un administrador puede filtrar extensionistas por ciudad, revisar las propiedades a su cargo, inspeccionar las encuestas levantadas en cada finca y finalmente descargar el PDF oficial de una encuesta aceptada.

> Todos los endpoints están bajo el prefijo `https://{backend}/api/v1/admin`. Usa un token JWT válido en el encabezado `Authorization: Bearer <token>`.

## 1. Filtrar extensionistas por ciudad

```bash
curl -X GET "https://{backend}/api/v1/admin/extensionists/names-ids-phones?city=Santa%20Marta" \
     -H "Authorization: Bearer $ADMIN_TOKEN"
```

Respuesta (ejemplo):
```json
{
  "status": "success",
  "message": "Extensionist names, identification, and phones list fetched successfully",
  "data": [
    {
      "id": 12,
      "name": "Laura Pérez",
      "identification": "1029384756",
      "phone": "3001234567",
      "city": "Santa Marta"
    }
  ]
}
```

## 2. Listar propiedades de un extensionista

```bash
curl -X GET "https://{backend}/api/v1/admin/extensionists/12/product-properties" \
     -H "Authorization: Bearer $ADMIN_TOKEN"
```

Esta llamada devuelve las fincas/propiedades en las que el extensionista 12 ha trabajado.

## 3. Consultar encuestas por propiedad (con enlace al PDF)

```bash
curl -X GET "https://{backend}/api/v1/admin/properties/45/surveys" \
     -H "Authorization: Bearer $ADMIN_TOKEN"
```

Aquí `45` corresponde al `property_id` obtenido en el paso anterior. La respuesta indica los `survey_id` y el tipo de encuesta aplicada a esa finca.
Cada elemento incluye `pdf_url`, que apunta al archivo oficial cuando ya fue generado (o una cadena vacía si aún no existe).

## 4. Ver detalle completo de una encuesta

```bash
curl -X GET "https://{backend}/api/v1/admin/surveys/1/21" \
     -H "Authorization: Bearer $ADMIN_TOKEN"
```

Esta petición retorna todo el contenido capturado en la encuesta tipo 1 con ID `21`, incluyendo datos del productor, la propiedad, recomendaciones y fotografías (el enlace al PDF ya viene en los listados anteriores).

## 5. Descargar el PDF oficial

```bash
curl -L -X GET "https://{backend}/api/v1/admin/surveys/1/21/pdf" \
     -H "Authorization: Bearer $ADMIN_TOKEN" \
     -o survey_1_21.pdf
```

El endpoint fuerza la generación del archivo si aún no existe, valida su presencia en `images/pdf/` y lo entrega como descarga directa. Guarda el PDF localmente (en el ejemplo, `survey_1_21.pdf`) para archivarlo o compartirlo.

Con estos pasos el administrador puede navegar todo el flujo: filtrar extensionistas por ciudad, identificar las fincas intervenidas, auditar las encuestas realizadas y obtener el PDF oficial correspondiente.
