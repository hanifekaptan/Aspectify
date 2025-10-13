import whisper

def whisper_tiny() -> whisper.Whisper:
    """
    Loads the tiny Whisper model

    Args:
        None

    Returns:
        whisper.Whisper: The tiny Whisper model
    """
    return whisper.load_model("tiny")

def whisper_base() -> whisper.Whisper:
    """
    Loads the base Whisper model

    Args:
        None

    Returns:
        whisper.Whisper: The base Whisper model
    """
    return whisper.load_model("base")

def whisper_small() -> whisper.Whisper:
    """
    Loads the small Whisper model

    Args:
        None

    Returns:
        whisper.Whisper: The small Whisper model
    """
    return whisper.load_model("small")

def whisper_medium() -> whisper.Whisper:
    """
    Loads the medium Whisper model

    Args:
        None

    Returns:
        whisper.Whisper: The medium Whisper model
    """
    return whisper.load_model("medium")

def whisper_large() -> whisper.Whisper:
    """
    Loads the large Whisper model

    Args:
        None

    Returns:
        whisper.Whisper: The large Whisper model
    """
    return whisper.load_model("large")
