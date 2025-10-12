import os

from app.ai_models.openai_whisper_models import whisper_tiny

model = whisper_tiny

def transcribe_from_path(audio_file_path: str) -> str:
    if not os.path.exists(audio_file_path):
        raise FileNotFoundError(f"Audio file not found: {audio_file_path}")

    try:
        result = model.transcribe(audio_file_path)
        return result["text"]
    except Exception as e:
        raise RuntimeError(f"Audio transcription error: {e}")
