# Request Lifecycle and Data Flow

This document describes the process from the moment a user sends a request to the Aspectify API until they receive a processed response, and explains the journey of data within the system.

## High-Level Flow

The data flow in the system occurs across logical layers:

1.  **API Layer**: The user's request is received, authenticated, and validated using Pydantic models.
2.  **Core Logic & Services Layer**: The validated data is directed to Agents and services for processing. Analysis and all other operations take place in this layer.
3.  **Data Layer**: Data required during the process is accessed.
4.  **API Layer**: The data obtained from the process is formatted using Pydantic models and returned to the user as a standard JSON response.

## Detailed Process Steps

The analysis process in the Core Logic layer consists of five main steps:

### 1. Input Processing

Every request that enters the system first goes through a step to determine its content type (e.g., `text`, `audio file`). Then, the language of the content is detected to prepare it for the subsequent steps.

```
User Input → Content Type Identification → Language Detection
```

### 2. Content Preparation

If the incoming content is an audio file, it is transcribed into text using the `Whisper` model. If the content is already in text format, this step is skipped, and the process moves on to language detection.

```
Audio File → Transcription → Text → Language Detection
```
```
Text → Language Detection
```

### 3. Language Detection

Before the prepared text is sent to the Aspect-Based Sentiment Analysis (ABSA) tool, the language of the content is detected. A response in the appropriate language is returned based on the detected language.


### 4. Analysis Process

The prepared text and the acquired language information are sent to the Aspect-Based Sentiment Analysis (ABSA) tool. This tool uses the `Gemini` LLM model to perform the analysis, extracting the sentiment and aspects from the text to produce a raw result.

```
Text → ABSA Tool → LLM Model → Result
```

### 5. Result Formatting

The raw result obtained from the analysis process is converted into a structured and consistent format using predefined Pydantic schemas. Finally, this structure is presented to the user as a standard JSON response via the API.

```
Raw Result → Pydantic Model → JSON Response
```