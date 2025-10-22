# Technology Stack

The main components used in the Aspectify project are listed below, grouped by their area of responsibility.

## App

- **Python 3.10**: The main programming language for the project. It was chosen for its modern syntax and rich library ecosystem.
- **FastAPI**: A high-performance, modern web framework. It is used for its asynchronous capabilities and automatic API documentation generation.
- **Pydantic**: Used for data validation, serialization, and type safety. It manages request and response models at the API layer.

## AI/ML

- **Google Gemini**: The core Large Language Model (LLM) used for advanced language understanding and aspect-based sentiment analysis tasks.
- **OpenAI Whisper**: The model used for high-accuracy speech-to-text transcription from audio files.
- **LangChain**: A framework used to easily manage and chain AI models, tools, and workflows.

## Infrastructure and Database

- **Docker**: Used for containerization to ensure the application and all its dependencies run consistently across different environments.
- **PostgreSQL**: The relational database used for storing structured data and main application data.
- **Pinecone**: The vector database used for efficiently storing and querying vector embeddings.
- **MkDocs**: A tool used to build a static website from Markdown files for project documentation.
- **GitHub Pages**: Used for publishing and hosting the generated documentation.