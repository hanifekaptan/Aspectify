
# Response Models

The Aspectify API uses structured and type-safe response models.

## Overview

All API responses are validated and serialized using Pydantic models. This ensures type safety, automatic validation, and API documentation.

## Main Response Models

### ABSAResponse

The main aspect-based sentiment analysis response model.

```python
class ABSAResponse(BaseModel):
    id: str
    polarity: str
    score: float
    aspects: List[AspectAnalysisResponse]
    message: str
    text: str
```

#### Fields

| Field | Type | Description |
|------|-----|----------|
| `id` | `str` | Unique analysis ID (UUID) |
| `polarity` | `str` | Overall sentiment (positive/negative/neutral) |
| `score` | `float` | Confidence score (0.0-1.0) |
| `aspects` | `List[AspectAnalysisResponse]` | List of aspect analyses |
| `message` | `str` | Operation status message |
| `text` | `str` | The analyzed text |

#### Example

```json
{
  "id": "123e4567-e89b-12d3-a456-426614174000",
  "polarity": "neutral",
  "score": 0.5,
  "aspects": [
    {
      "aspect": "camera",
      "sentiment": "positive",
      "score": 0.95,
      "quote": "the camera is great"
    }
  ],
  "message": "ABSA completed successfully.",
  "text": "The camera of this phone is great."
}```

### AspectAnalysisResponse

The aspect analysis response model.

```python
class AspectAnalysisResponse(BaseModel):
    aspect: str
    sentiment: str
    score: float
    quote: str
```

#### Fields

| Field | Type | Description |
|------|-----|----------|
| `aspect` | `str` | Name of the aspect (e.g., "camera", "battery") |
| `sentiment` | `str` | Sentiment of the aspect (positive/negative/neutral) |
| `score` | `float` | Confidence score (0.0-1.0) |
| `quote` | `str` | The relevant quote from the text |

#### Example

```json
{
  "aspect": "camera",
  "sentiment": "positive",
  "score": 0.95,
  "quote": "the camera takes great photos"
}
```

### LLMResponse

The LLM model response model.

```python
class LLMResponse(BaseModel):
    polarity: str
    score: float
    aspects: List[AspectAnalysisResponse]
```

#### Fields

| Field | Type | Description |
|------|-----|----------|
| `polarity` | `str` | Overall sentiment (positive/negative/neutral) |
| `score` | `float` | Confidence score (0.0-1.0) |
| `aspects` | `List[AspectAnalysisResponse]` | List of aspect analyses |

#### Example

```json
{
  "polarity": "positive",
  "score": 0.8,
  "aspects": [
    {
      "aspect": "quality",
      "sentiment": "positive",
      "score": 0.9,
      "quote": "the quality is very good"
    }
  ]
}
```

## Request Models

### MultiModalRequest

The multi-modal request model.

```python
class MultiModalRequest(BaseModel):
    data: str
    language: Optional[str] = None
```

#### Fields

| Field | Type | Description |
|------|-----|----------|
| `data` | `str` | The text or file path to be analyzed |
| `language` | `Optional[str]` | Optional language code |

#### Example

```json
{
  "data": "This product is truly great!",
  "language": "tr"
}
```

## Data Types

### Sentiment Types

```python
from typing import Literal

PolarityType = Literal["positive", "negative", "neutral"]
SentimentType = Literal["positive", "negative", "neutral"]
```

**Values:**
- `positive`: Positive sentiment
- `negative`: Negative sentiment
- `neutral`: Neutral sentiment

### Content Types

```python
from typing import Literal

ContentType = Literal["text", "audio_path"]
```

**Values:**
- `text`: Plain text
- `audio_path`: Audio file path

## Validation Rules

### ABSAResponse Validation

```python
class ABSAResponse(BaseModel):
    id: str = Field(..., description="Unique analysis ID")
    polarity: str = Field(..., regex="^(positive|negative|neutral)$")
    score: float = Field(..., ge=0.0, le=1.0, description="Confidence score")
    aspects: List[AspectAnalysisResponse] = Field(..., min_items=0)
    message: str = Field(..., min_length=1)
    text: str = Field(..., min_length=1)```

### AspectAnalysisResponse Validation

```python
class AspectAnalysisResponse(BaseModel):
    aspect: str = Field(..., min_length=1, description="Name of the aspect")
    sentiment: str = Field(..., regex="^(positive|negative|neutral)$")
    score: float = Field(..., ge=0.0, le=1.0, description="Confidence score")
    quote: str = Field(..., min_length=1, description="Quote from the text")
```

## Serialization

### JSON Serialization

```python
# Convert the model to JSON
response = ABSAResponse(...)
json_data = response.model_dump_json()

# Create a model from JSON
json_str = '{"id": "123", "polarity": "positive", ...}'
response = ABSAResponse.model_validate_json(json_str)
```

### Dict Serialization

```python
# Convert the model to a dict
response = ABSAResponse(...)
dict_data = response.model_dump()

# Create a model from a dict
dict_data = {"id": "123", "polarity": "positive", ...}
response = ABSAResponse.model_validate(dict_data)
```