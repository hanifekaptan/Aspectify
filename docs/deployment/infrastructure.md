# Environment Requirements

This document defines the environment required to run the Aspectify platform in its current state, as well as the planned infrastructure for the project's future goals.

## Current Status: Basic Requirements

To run the current version of the project, it is sufficient to have the following software installed on your system:

-   **Python:** `3.10` or higher.
-   **pip:** To install Python packages (uses the `requirements.txt` file).
-   **Git:** To download the project code.

### External Dependencies

The application's core analysis logic requires valid API keys to access the following external services. It is mandatory to configure these keys in the `.env` file:

-   **Google Gemini API Key**
-   **OpenAI Whisper API Key**

## Future Plans: Planned Infrastructure

The project's roadmap includes the following technologies to make it a more scalable and robust service. This document will be updated as these components are added.

-   **Containerization (Docker):** Docker and Docker Compose integration is planned to ensure that the application and its dependencies run consistently across any environment.
-   **Data Layer (Database):** PostgreSQL (for structured data) and Pinecone (for vector data) databases will be added to permanently store analysis results and enable more complex queries.
-   **API Layer (FastAPI):** A REST API interface will be developed using FastAPI so that the application can be easily consumed by external services.