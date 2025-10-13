from typing import Literal

ContentType = Literal["text", "audio_path"]

def identify_content_type(data: str) -> ContentType:
    """
    Determines if a string is a file path to an audio file or plain text.
    This is a fast, rule-based check.

    Args: 
        data (str): The string to be checked.

    Returns:
        ContentType: "text" if the string is plain text, "audio_path" if it's a file path to an audio file.
    """
    audio_extensions = [".wav", ".mp3", ".m4a", ".flac"]
    if any(data.endswith(ext) for ext in audio_extensions):
        return "audio_path"
    return "text"
