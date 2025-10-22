# Quick Start

This guide will help you perform your first sentiment analysis with Aspectify.

## Basic Usage

### 1. Text Analysis

The simplest way to use the application:

```python
import asyncio
from app.agents.absa_agent import run_absa

async def main():
    text = "This phone's camera is great, but its battery is very bad."
    result = await run_absa(text)
    
    print(f"Overall Sentiment: {result.polarity}")
    print(f"Confidence Score: {result.score}")
    print("Aspects:")
    for aspect in result.aspects:
        print(f"  - {aspect.aspect}: {aspect.sentiment} ({aspect.score})")

asyncio.run(main())
```

### 2. Audio File Analysis

You can also analyze audio files:

```python
import asyncio
from app.agents.absa_agent import run_absa

async def main():
    audio_path = "path/to/your/audio.wav"
    result = await run_absa(audio_path)
    
    print(f"Transcription: {result.text}")
    print(f"Overall Sentiment: {result.polarity}")
    print(f"Confidence Score: {result.score}")

asyncio.run(main())
```

## Supported Formats

### Text Input
- Direct text string
- Text in any language

### Audio Files
- `.wav` - WAV format
- `.mp3` - MP3 format
- `.m4a` - M4A format
- `.flac` - FLAC format

## Example Output

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
    },
    {
      "aspect": "battery",
      "sentiment": "negative",
      "score": 0.98,
      "quote": "its battery is very bad"
    }
  ],
  "message": "ABSA completed successfully.",
  "text": "This phone's camera is great, but its battery is very bad."
}
```

## Sentiment Types

### Polarity (Overall Sentiment)
- `positive`: Positive sentiment
- `negative`: Negative sentiment
- `neutral`: Neutral sentiment

### Sentiment (Aspect Sentiment)
- `positive`: Positive
- `negative`: Negative
- `neutral`: Neutral

## Confidence Scores

Scores range from 0.0 to 1.0:

- **0.0 - 0.3**: Low confidence
- **0.3 - 0.7**: Medium confidence
- **0.7 - 1.0**: High confidence

## Quick Test

Run a quick test using the provided test data:

```bash
python main.py
```

This command analyzes the sample texts in the `test_data/text/test_texts.jsonl` file.

## Advanced Usage

### Specifying a Custom Language

Although language detection is handled automatically by integrated modules, you can specify the desired language input as shown below.

```python
from app.tools.absa_analyzer import absa_analyzer_tool

result = absa_analyzer_tool.invoke({
    "text": "This product is truly great!",
    "language": "tr"
})

result = absa_analyzer_tool.invoke({
    "text": "This product is amazing!",
    "language": "en"
})
```

### Batch Analysis

```python
import asyncio
from app.agents.absa_agent import run_absa

async def analyze_multiple_texts(texts):
    results = []
    for text in texts:
        result = await run_absa(text)
        results.append(result)
    return results

texts = [
    "This phone is great!",
    "The camera quality is bad.",
    "The price is reasonable, but the performance is inadequate."
]

results = asyncio.run(analyze_multiple_texts(texts))
```

## Troubleshooting

### Common Errors

1. **API Key Error**: Check your Google API key in the `.env` file.
2. **Empty Text**: The text to be analyzed cannot be empty.
3. **Unsupported Format**: Check the audio file format.

### Performance Tips

1. **Batch Processing**: Process multiple texts at once.
2. **Caching**: Cache the results.
3. **Asynchronous Usage**: Use `async/await`.

## Next Steps

- [Architecture](../architecture/overview.md) - Learn about the system architecture
- [Development](../development/local-setup.md) - Read the development guide
- [Deployment](../deployment/infrastructure.md) - Learn about infrastructure requirements for deployment
- [API Reference](../api/endpoints.md) - Learn about the API endpoints