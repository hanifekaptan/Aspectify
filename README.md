# Aspectify
[![Read in Turkish](https://img.shields.io/badge/Language-Turkish-red)](./README_TR.md)
[![Project Status](https://img.shields.io/badge/status-in%20development-orange)](https://github.com/hanifekaptan/Aspectify)
[![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-Apache-green.svg)](LICENSE)

Aspectify is an advanced **Aspect-Based Sentiment Analysis (ABSA)** platform designed for multi-modal content like text and audio. Leveraging the power of modern AI models such as Google Gemini and OpenAI Whisper, it goes beyond simple positive/negative labels. Aspectify identifies specific "aspects" within a text and determines their unique sentiment trends.

This project was initiated as a personal development endeavor to explore modern AI engineering principles and clean architecture practices.

---

## ✨ Key Features

-   **🎯 Aspect-Based Analysis:** Correctly identifies that in "This phone's camera is great, but its battery is bad," the "camera" is positive, while the "battery" is negative.
-   **🎤 Multi-Modal Input:** Supports analysis of both plain text and audio files.
-   **🤖 Modern AI Integration:** Powered by state-of-the-art AI models like Google Gemini and OpenAI Whisper.
-   **🧩 Modular & Clean Architecture:** Features a maintainable and extensible codebase based on "Clean Code" and "Separation of Concerns" principles.
-   **📊 Detailed Outputs:** Provides rich results with overall polarity, confidence scores, a list of aspects, and relevant quotes.

## 🚀 Project Status

⚠️ **This project is under active development.** The core analysis logic and modular structure have been established. Features such as a REST API, Docker support, and database integration are on the roadmap.

## ⚙️ How It Works

Aspectify employs a modular, agent-driven architecture to process requests. The flow is orchestrated to handle different types of content intelligently.

**`User Input (Text/Audio) -> [1. Logic Layer] -> [2. Agent] -> [3. AI Tools] -> [4. Fused Response]`**

1.  **Logic Layer (`/logic`):** The first point of contact. It identifies the content type (text vs. audio) and detects the language. If the input is audio, it uses the **Transcription Tool** to convert it to text.
2.  **Orchestrator Agent (`/agents`):** The "brain" of the system. It receives the prepared text and decides which tools to use. It's responsible for invoking the analysis tool and ensuring the final output is structured correctly.
3.  **AI Tools (`/tools`):** These are specialized workers that perform core tasks. The main tool is the **ABSA Analyzer**, which uses the Gemini model to perform a detailed aspect-based analysis on the given text.
4.  **Structured Response (`/schemas`):** The agent takes the raw output from the AI tools and formats it into a clean, predictable JSON object using Pydantic models before returning it to the user.

## 🛠️ Technology Stack

| Category          | Core Technologies                    | Planned               |
| ----------------- | ------------------------------------ | --------------------- |
| **Backend**       | Python 3.10+                         | FastAPI               |
| **AI / ML**       | Google Gemini, OpenAI Whisper        | LangChain             |
| **Data Validation** | Pydantic                             | -                     |
| **Infrastructure**| -                                    | Docker, SQLite    |
| **Database**      | -                                    | Pinecone (Vector DB)  |

## 📂 Project Structure

The project follows a clean architecture to separate concerns, making it easy to navigate and extend.

```
Aspectify/
├── app/
│   ├── agents/         # Orchestrates the workflow (the "brain")
│   ├── ai_models/      # Low-level integration with AI models
│   ├── core/           # Configuration, logging, and core settings
│   ├── logic/          # Business logic (transcription, language detection)
│   ├── schemas/        # Pydantic models for request/response validation
│   └── tools/          # Specialized tools the agent can use (e.g., ABSA analyzer)
├── test_data/          # Sample data for testing
├── tests/              # Test suite (under development)
├── docs/               # Detailed project documentation
├── main.py             # Main entry point for running the application
├── requirements.txt
├── .env.example        # Environment variable template
└── README.md
```

## 🚀 Getting Started

Follow these steps to get the project running on your local machine.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/hanifekaptan/Aspectify.git
    cd Aspectify
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    ```
3.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Configure your API keys:**
    Copy `.env.example` to `.env` and enter your unique API keys.
    ```bash
    cp .env.example .env
    ```

For detailed setup and usage instructions, please refer to the full documentation.

## 📖 Full Documentation

All details about the project's architecture, development standards, and future plans are available in our comprehensive documentation.

➡️ **[Read the Project Documentation](./docs/README.md)**

## 🤝 Contributing

While this is a personal development project, ideas and suggestions are always welcome. If you'd like to contribute, please review the **[Development Guide](./docs/development/README.md)**.

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.
