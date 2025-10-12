from app.schemas.response.aspect_response import AspectAnalysisResponse
from pydantic import BaseModel, Field
from typing import List

class LLMResponse(BaseModel):
    """
    Aspect Based Sentiment Analysis (ABSA) Response
    
    polarity: str = General sentiment (positive, negative, neutral)
    score: float = Sentiment score (0.0-1.0)
    aspects: List[AspectAnalysisResponse] = List of extracted aspects
    text: str = Input text
    """
    polarity: str = Field(..., description="General sentiment (positive, negative, neutral)")
    score: float = Field(..., description="Sentiment score (0.0-1.0)")
    aspects: List[AspectAnalysisResponse] = Field(..., description="List of extracted aspects")
