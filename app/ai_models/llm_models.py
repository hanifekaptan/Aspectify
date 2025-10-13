import os
from langchain_google_genai import ChatGoogleGenerativeAI

from app.core.config import settings

if settings.GOOGLE_API_KEY:
    os.environ["GOOGLE_API_KEY"] = settings.GOOGLE_API_KEY.get_secret_value()

def load_gemini_2_5_pro_model() -> ChatGoogleGenerativeAI:
    """
        Loads the Gemini 2.5 Pro model from Google.
        This model is used for sentiment analysis and aspect extraction.

        Args:
            None

        Returns:
            ChatGoogleGenerativeAI: The Gemini 2.5 Pro model.
    """
    try:
        return ChatGoogleGenerativeAI(
            model=settings.GEMINI_2_5_PRO_MODEL,
            api_version="v1",
            temperature=0.1,
            max_output_tokens=8192,
        )
    except Exception as e:
        raise ValueError(f"Error: {e}")

gemini_2_5_pro = load_gemini_2_5_pro_model()
