from pydantic import BaseModel, Field

class AspectAnalysisResponse(BaseModel):
    """
    Aspect Analysis Response
    
    aspect: str = Extracted aspect
    sentiment: str = Sentiment of the aspect (positive, negative, neutral)
    score: float = Sentiment score (0.0-1.0)
    quote: str = Quote of the aspect
    """
    aspect: str = Field(..., description="Extracted aspect")
    sentiment: str = Field(..., description="Sentiment of the aspect (positive, negative, neutral)")
    score: float = Field(..., description="Sentiment score (0.0-1.0)")
    quote: str = Field(..., description="Quote of the aspect")
    