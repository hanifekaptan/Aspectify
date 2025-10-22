# Aspectify

**An Aspect-Based Sentiment Analysis (ABSA) Application**

Aspectify is an application that performs aspect-based sentiment analysis on text and audio content using Google's Gemini AI models. By analyzing sentiments for different aspects within the same text, it provides detailed insights into user opinions.

## Features

- 🎯 **Aspect-Based Analysis**: Detects aspects within the text and performs sentiment analysis for each one.
- 🎤 **Audio Support**: Transcribes audio files to include them in the analysis process.
- 🌍 **Multi-language Support**: Dynamically determines the content language and supports multiple languages.
- 🤖 **AI-Powered**: Uses Google Gemini models for sentiment analysis.
- 📊 **Detailed Results**: Provides detailed output including polarity, confidence scores, aspects, and quotes.
- 📝 **Logging**: Implements application logging for debugging and monitoring.

## Quick Start

```python
from app.agents.absa_agent import run_absa

text = "The camera is great, but the battery life is bad."

result = await run_absa(text)
print(f"Overall sentiment: {result.polarity}")
print(f"Confidence: {result.score}")
for aspect in result.aspects:
    print(f"{aspect.aspect}: {aspect.sentiment} ({aspect.score})")
```

## Architecture

Aspectify follows a modular architecture:
- **agents**: Manages analysis workflows and the agent structure.
- **ai_models**: Defines integrations for Google Gemini and OpenAI Whisper models.
- **tools**: Provides specialized analysis tools and utilities.
- **logic**: Contains the core business logic for content processing.
- **schemas**: Defines the data models.
- **core**: Establishes the configuration and logging infrastructure.

## Getting Started

1. [Installation](getting-started/installation.md) - Set up the development environment
2. [Configuration](getting-started/configuration.md) - Configure the settings
3. [Quick Start](getting-started/quick-start.md) - Run your first analysis

## Documentation

1. **Architecture:** This section covers the design principles and overall structure of the system. It details the main components and their interactions. It provides information on the technology stack, including programming languages, frameworks, and databases. Additionally, it explains the main folder structure, the responsibilities of each module, and outlines the lifecycle of an API request within the system.

2. **Development Guide:** This guide, aimed at those looking to contribute to the project's codebase, covers the entire development process. It provides a step-by-step explanation of how to set up the local environment for a developer to work on their machine. It defines the coding standards and linter rules that must be followed to ensure code consistency across the project. Finally, it demonstrates how to prepare and run tests to ensure the quality and correctness of the written code.

3. **Deployment Guide:** This guide focuses on the process of deploying the application to a live production environment where it will serve end-users. It specifies the requirements for servers, databases, and other infrastructure services needed for the application to run smoothly. It describes production-specific configuration steps and how to set environment variables. It also explains how to configure the logging mechanism to track events and potential errors that occur while the system is running.

4. **API Reference:** This technical reference, which defines how the application communicates with the outside world, details the usage of the API. It includes all available API endpoints, such as `GET /agents` and `POST /tasks`, and their functions. It presents the data models (schemas) that define the structure of the request and response bodies used for data exchange with the API. (Note: This section is currently under development.)

## Example Output

```json
{
  "id": "uuid-goes-here",
  "polarity": "neutral",
  "score": 0.5,
  "aspects": [
    {
      "aspect": "camera",
      "sentiment": "positive",
      "score": 0.95,
      "quote": "the camera is great"
    },
    {
      "aspect": "battery",
      "sentiment": "negative", 
      "score": 0.98,
      "quote": "the battery life is bad"
    }
  ],
  "message": "ABSA completed successfully.",
  "text": "The camera is great, but the battery life is bad."
}
```

## Support

For questions, issues, or contributions, please visit the [GitHub repository](https://github.com/hanifekaptan/Aspectify). You can also contact me directly via [Linkedin](https://medium.com/@hanifekaptan) or [E-mail](mailto:hanifekaptan.dev@gmail.com).
