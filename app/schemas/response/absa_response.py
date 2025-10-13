from pydantic import BaseModel, Field
from typing import List
import uuid

from app.schemas.response.aspect_response import AspectAnalysisResponse

quote: str = Field(..., description="Quote of the aspect")

class ABSAResponse(BaseModel):
    """
    Aspect Based Sentiment Analysis (ABSA) Response
    
    id: str = unique identifier
    polarity: str = General sentiment (positive, negative, neutral)
    score: float = Sentiment score (0.0-1.0)
    aspects: List[AspectAnalysisResponse] = List of extracted aspects
    message: str = Response message
    text: str = Input text
    """
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    polarity: str = Field(..., description="General sentiment (positive, negative, neutral)")
    score: float = Field(..., description="Sentiment score (0.0-1.0)")
    aspects: List[AspectAnalysisResponse] = Field(..., description="List of extracted aspects")
    message: str = Field(..., description="Response message")
    text: str = Field(..., description="Input text")
