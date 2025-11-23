# PUT /surveys/3/{survey_id}

Update a Survey 3 (cierre de acompañamiento) that is in `rejected` state. After updating, the state returns to `pending`.

## Request
- **Method:** `PUT`
- **Path:** `/surveys/3/{survey_id}`
- **Content-Type:** `multipart/form-data`

| Form Field | Type | Required | Description |
|------------|------|----------|-------------|
| `api_key` | `string` | Yes | API key of the extensionist. |
| `survey_data` | `string` (JSON) | Yes | Fields that map to `UpdateSurvey3InputDTO`. |
| `classification_user` | `string` (JSON) | No | Updated JSON for the `survey_3.classification_user` column. |
| `producter_data` | `string` (JSON) | Yes | Same payload used on POST `/surveys/3`. |
| `property_data` | `string` (JSON) | Yes | Same payload used on POST `/surveys/3`. |
| `files` | `List[UploadFile]` | No | Replacement images (user, interaction, panorama, extra). |

### Example `survey_data`
```json
{
  "classification_user": {
    "development_human_capacity": {"observation": "Final adjustments", "score": 5},
    "development_social_capacity": {"observation": "Maintains leadership", "score": 4},
    "access_adaptative_adoption_information": {"observation": "Consults technical bulletins", "score": 5},
    "sustainable_management_natural_resources": {"observation": "Implements soil conservation", "score": 4},
    "participation_public_political": {"observation": "Represents local board", "score": 3}
  },
  "medition_focalization": {
    "control_resources": {
      "score": 4,
      "obervation": "Notas actualizadas"
    }
  },
  "objetive_accompaniment": "Objetivo actualizado",
  "development_accompaniment": "Descripción nueva",
  "final_diagnosis": "Diagnóstico final actualizado",
  "recommendations_commitments": "Compromisos finales",
  "observations_visited": "Observaciones finales",
  "visit_date": "2025-12-01T09:00:00Z",
  "attended_by": "Coordinador Acompañamiento"
}
```

## Example cURL
```bash
curl -X PUT "https://api.example.com/surveys/3/44" \
  -H "Content-Type: multipart/form-data" \
  -F 'api_key=EXT-123' \
  -F 'classification_user={
        "development_human_capacity": {"observation": "Final adjustments", "score": 5},
        "development_social_capacity": {"observation": "Maintains leadership", "score": 4},
        "access_adaptative_adoption_information": {"observation": "Consults technical bulletins", "score": 5},
        "sustainable_management_natural_resources": {"observation": "Implements soil conservation", "score": 4},
        "participation_public_political": {"observation": "Represents local board", "score": 3}
      }' \
  -F 'survey_data={
        "medition_focalization": {
          "control_resources": {
            "score": 4,
            "obervation": "Notas actualizadas"
          }
        },
        "objetive_accompaniment": "Objetivo actualizado",
        "development_accompaniment": "Descripción nueva",
        "final_diagnosis": "Diagnóstico final actualizado",
        "recommendations_commitments": "Compromisos finales",
        "observations_visited": "Observaciones finales",
        "visit_date": "2025-12-01T09:00:00Z",
        "attended_by": "Coordinador Acompañamiento"
      }' \
  -F 'producter_data={
        "id": 2,
        "name": "John Doe",
        "type_id": "1",
        "identification": "123456789"
      }' \
  -F 'property_data={
        "id": 2,
        "name": "La Esperanza Farm",
        "latitude": "11.23",
        "longitude": "-74.20"
      }' \
  -F 'files=@/path/to/photo_user.jpg' \
  -F 'files=@/path/to/photo_interaction.jpg' \
  -F 'files=@/path/to/photo_panorama.jpg' \
  -F 'files=@/path/to/photo_extra.jpg'
```
