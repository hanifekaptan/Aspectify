import uuid

from app.schemas.response.absa_response import ABSAResponse
from app.tools.absa_analyzer import absa_analyzer_tool
from app.logic.transcriber import transcribe_from_path
from app.logic.language_detector import detect_content_language
from app.logic.content_type_identifier import identify_content_type

async def run_absa(
    data: str
    ) -> ABSAResponse:
    """
    Runs aspect-based sentiment analysis on the input text or audio file.

    Steps:
    1. Checks if the input is an audio file or plain text.
    2. Transcribes the audio file to text if it's an audio file.
    3. Detects the language of the text.
    4. Runs ABSA analysis on the text.

    Args:
        data (str): The text or audio file path to be analyzed.

    Returns:
        ABSAResponse: The Pydantic object containing the analysis results.
    """
    content_type = identify_content_type(data)
    text_content = ""
    is_audio_path = (content_type == "audio_path")
    
    if is_audio_path:
        text_content = transcribe_from_path(data)
    else:
        text_content = data

    if not text_content:
        raise ValueError("The text content to be analyzed cannot be empty.")

    language = detect_content_language(text_content)
    result = absa_analyzer_tool.invoke({"text": text_content, "language": language})
    final_response = ABSAResponse(
        id=str(uuid.uuid4()),
        polarity=result["polarity"],
        score=result["score"],
        aspects=result["aspects"],
        message="ABSA completed successfully.",
        text=text_content
    )
    return final_response