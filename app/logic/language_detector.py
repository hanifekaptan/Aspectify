from langdetect import detect, LangDetectException

def detect_content_language(text: str) -> str:
    """
    Detects the language of a given text using a lightweight library.
    Returns a language code (e.g., 'tr', 'en').

    Args:
        text (str): The text to detect the language of.

    Returns:
        str: The detected language code.
    """
    try:
        if len(text.split()) < 3:
            return "unknown"
        return detect(text)
    except LangDetectException:
        return "unknown"