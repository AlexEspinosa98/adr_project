# PUT Requests Overview

The legacy single `PUT /surveys/{survey_type}/{id}` endpoint was split into three explicit routes:

- `/surveys/1/{survey_id}` – documented in `put_1.md`
- `/surveys/2/{survey_id}` – documented in `put_2.md`
- `/surveys/3/{survey_id}` – documented in `put_3.md`

Each file contains the payload description plus a ready-to-use `curl` example. Refer to those guides for the exact `multipart/form-data` format expected by each survey type.
