# System Architecture

Aspectify is a sentiment analysis platform developed using a modern Python architecture.

## Overall Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Aspectify Platform                       │
├─────────────────────────────────────────────────────────────┤
│  API Layer (FastAPI)                                        │
│  ├── Endpoints & Authentication                             │
│  └── Request/Response Models                                │
├─────────────────────────────────────────────────────────────┤
│  Core Logic & Services Layer                                │
│  ├── Agents (Orchestration & Business Rules)                │
│  ├── Business Services (e.g., AnalysisService)              │
│  └── AI/ML Services (Internal Wrappers)                     │
│      ├── LLM Service (Gemini)                               │
│      └── Transcription Service (Whisper)                    │
├─────────────────────────────────────────────────────────────┤
│  Data Layer                                                 │
│  ├── Database (PostgreSQL, Pinecone)                        │
│  └── File Storage                                           │
└─────────────────────────────────────────────────────────────┘
```

## Module Structure

### 🏗️ Core
```
app/core/
├── config.py          # Configuration management
└── logging_config.py  # Logging configuration
```

**Responsibilities:**
- Application configuration
- Environment variable management
- Logging system

### 🤖 Agents
```
app/agents/
└── absa_agent.py      # Main ABSA analysis agent
```

**Responsibilities:**
- Workflow management
- Data processing coordination
- Result formatting

### 🧠 AI Models
```
app/ai_models/
├── llm_models.py           # LLM model management
└── openai_whisper_models.py # Whisper model management
```

**Responsibilities:**
- AI model connections
- Model configuration

### 🔧 Logic
```
app/logic/
├── content_type_identifier.py  # Content type identification
├── language_detector.py        # Language detection
└── transcriber.py              # Audio transcription
```

**Responsibilities:**
- Content type analysis
- Language detection
- Audio file processing

### 🛠️ Tools
```
app/tools/
└── absa_analyzer.py    # ABSA analysis tool
```

**Responsibilities:**
- Sentiment analysis processing
- Aspect identification
- Result formatting

### 📋 Schemas
```
app/schemas/
├── request/
│   └── multi_modal_request.py  # Request models
└── response/
    ├── absa_response.py        # ABSA response model
    ├── aspect_response.py      # Aspect response model
    └── llm_response.py         # LLM response model
```

**Responsibilities:**
- Data validation
- API contracts
- Type safety

## Data Flow

### 1. Input Processing
```
User Input → Content Type Identification → Language Detection
```

### 2. Content Preparation
```
Audio File → Transcription → Text
Text → Direct Processing
```

### 3. Analysis Process
```
Text → ABSA Tool → LLM Model → Result
```

### 4. Result Formatting
```
Raw Result → Pydantic Model → JSON Response
```

## Technology Stack

### Backend
- **Python 3.10**: Main programming language
- **FastAPI**: Web framework
- **Pydantic**: Data validation

### AI/ML
- **Google Gemini**: LLM model
- **OpenAI Whisper**: Speech-to-text transcription
- **LangChain**: AI framework

### Infrastructure
- **Docker**: Containerization
- **MkDocs**: Documentation
- **GitHub Pages**: Documentation hosting

## Future Plans

### Short-Term
- [ ] API endpoints and validation
- [ ] Language detection independent of the application flow
- [ ] Caching step
- [ ] Text preprocessing before analysis
- [ ] Web interface
- [ ] Structural and vector database setup
- [ ] Logging setup

### Long-Term
- [ ] Task scoping with advanced prompt structures
- [ ] Advanced analysis
- [ ] Visual analysis
- [ ] Backend enhancements