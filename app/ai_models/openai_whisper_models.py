import whisper

def whisper_tiny():
    return whisper.load_model("tiny")

def whisper_base():
    return whisper.load_model("base")

def whisper_small():
    return whisper.load_model("small")

def whisper_medium():
    return whisper.load_model("medium")

def whisper_large():
    return whisper.load_model("large")
