# PUT /surveys/2/{survey_id}

Update a Survey 2 entry that is currently `rejected`. After applying changes the survey state returns to `pending`.

## Request
- **Method:** `PUT`
- **Path:** `/surveys/2/{survey_id}`
- **Content-Type:** `multipart/form-data`

| Form Field | Type | Required | Description |
|------------|------|----------|-------------|
| `api_key` | `string` | Yes | API key of the extensionist. |
| `survey_data` | `string` (JSON) | Yes | Fields following `UpdateSurvey2InputDTO`. |
| `classification_user` | `string` (JSON) | No | Optional JSON for parity with other surveys. Survey 2 currently does not persist this field. |
| `producter_data` | `string` (JSON) | Yes | Same payload used when creating Survey 2. |
| `property_data` | `string` (JSON) | Yes | Same payload used when creating Survey 2. |
| `files` | `List[UploadFile]` | No | Optional replacement photos (user, interaction, panorama, extra). |

### Example `survey_data`
```json
{
  "objective_accompaniment": "Seguimiento al plan",
  "visit_development_follow_up_activities": "Descripción de actividades",
  "previous_visit_recommendations_fulfilled": true,
  "recommendations_commitments": "Nuevos compromisos",
  "observations_visited": "Observaciones recientes",
  "visit_date": "2025-11-10T11:00:00Z",
  "attended_by": "Alex Espinosa"
}
```

## Example cURL
```bash
curl -X PUT "https://api.example.com/surveys/2/25" \
  -H "Content-Type: multipart/form-data" \
  -F 'api_key=EXT-123' \
  -F 'survey_data={
        "objective_accompaniment": "Seguimiento al plan",
        "visit_development_follow_up_activities": "Descripción de actividades",
        "previous_visit_recommendations_fulfilled": true,
        "recommendations_commitments": "Nuevos compromisos",
        "observations_visited": "Observaciones recientes",
        "visit_date": "2025-11-10T11:00:00Z",
        "attended_by": "Alex Espinosa"
      }' \
  -F 'producter_data={
        "id": 12,
        "name": "Jane Doe",
        "type_id": "2",
        "identification": "555888999",
        "number_phone": "3100000000"
      }' \
  -F 'property_data={
        "id": 8,
        "name": "Finca San Pedro",
        "latitude": "11.25",
        "longitude": "-74.15",
        "state": "Magdalena",
        "city": "Santa Marta"
      }' \
  -F 'files=@/path/to/photo_user.jpg' \
  -F 'files=@/path/to/photo_interaction.jpg'
```
