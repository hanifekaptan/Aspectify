# API Endpoints

This document defines the planned RESTful endpoints for the Aspectify API.

**⚠️ Current Status:** This API is still under development, and these endpoints are not yet active. This document serves as a roadmap to define the project's API vision and future interface.

---

## Planned Endpoints

### Initiate Analysis

-   **Endpoint:** `POST /analyze`
-   **Description:** Initiates a new text or audio analysis task. This is the main functional endpoint of the system.
-   **Request Body:** Expects a JSON object conforming to the `MultiModalRequest` schema.
-   **Successful Response (200 OK):** Returns a JSON object conforming to the `ABSAResponse` schema.

**Example Request (`curl`):**

```bash
curl -X POST "http://localhost:8000/analyze" \
-H "Content-Type: application/json" \
-d '{
  "content": "The service was very fast, but the food was cold.",
  "content_type": "text"
}'
```

---

### Query Task Status (Future)

-   **Endpoint:** `GET /tasks/{task_id}`
-   **Description:** Planned for querying the status of asynchronous analysis tasks that may take a long time, such as large audio files.
-   **Request Body:** None.
-   **Successful Response (200 OK):** Returns a JSON object containing the status of the task ('PENDING', 'SUCCESS', 'FAILED') and, if successful, the analysis result.