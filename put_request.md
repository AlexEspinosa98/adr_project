# PUT Request: Update Survey 1

## Endpoint
- **Method:** `PUT`
- **Path:** `/surveys/1/{survey_id}`

Use this endpoint to edit an existing Survey 1 record. The survey must currently be in the `rejected` state; after a successful update the system automatically changes the state back to `pending`.

## Request Format
- **Content-Type:** `multipart/form-data`

| Form Field | Type | Required | Description |
|------------|------|----------|-------------|
| `api_key` | `string` | Yes | API key of the extensionist performing the update. |
| `survey_data` | `string` (JSON) | Yes | JSON payload that follows `UpdateSurvey1InputDTO`. Only supplied fields are changed. |
| `files` | `List[UploadFile]` | No | Up to 4 images. If supplied they replace, in order, `photo_user`, `photo_interaction`, `photo_panorama`, `phono_extra_1`. |

### Fields Accepted Inside `survey_data`
All fields are optional; omit those you do not need to change. `classification_user` cannot be edited.

- `medition_focalization` (object)
- `objetive_accompaniment` (string)
- `initial_diagnosis` (string)
- `recommendations_commitments` (string)
- `observations_visited` (string)
- `date_hour_end` (ISO datetime)
- `copy_documentation_delivered` (string / boolean-like flag)
- `date_acompanamiento` (string / ISO date)
- `hour_acompanamiento` (string / HH:MM)
- `origen_register` (string, e.g., `MOBILE` or `WEB`)
- `name_acompanamiento` (string)
- `type_acompanamiento` (string)
- `other_acompanamiento` (string)
- `visit_date` (ISO datetime)
- `attended_by` (string)
- `user` (string)
- `worker_up` (string)
- `household_size` (string)
- `other` (string)

### Example `survey_data`
```json
{
  "objetive_accompaniment": "Corrección al objetivo inicial de la visita",
  "recommendations_commitments": "Compromisos actualizados tras la retroalimentación.",
  "observations_visited": "Se añadió detalle adicional de las observaciones.",
  "date_hour_end": "2025-11-10T15:30:00",
  "copy_documentation_delivered": "true",
  "origen_register": "MOBILE",
  "visit_date": "2025-11-10T14:00:00",
  "attended_by": "Alex Espinosa",
  "household_size": "4"
}
```

### Example cURL
```bash
curl -X PUT "https://api.example.com/surveys/1/123" \
  -H "Content-Type: multipart/form-data" \
  -F 'api_key=EXT-123' \
  -F 'survey_data={
        "objetive_accompaniment": "Corrección al objetivo inicial de la visita",
        "recommendations_commitments": "Compromisos actualizados tras la retroalimentación."
      }' \
  -F 'files=@/path/to/photo_user.jpg' \
  -F 'files=@/path/to/photo_interaction.jpg'
```

### Successful Response
```json
{
  "status": "success",
  "message": "Survey 1 with ID 123 updated successfully and set to pending.",
  "data": {
    "id": 123,
    "state": "pending"
  }
}
```
