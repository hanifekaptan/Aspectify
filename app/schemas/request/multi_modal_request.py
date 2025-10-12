from pydantic import BaseModel, Field

class MultiModalRequest(BaseModel):
    """
    Text and Audio Multi-modal Input Schemas

    It defines the structure of the request and ensures that at least one input type (text or audio file) is provided.
 
    data: str = Text or audio file path
    language: str = Language code for text analysis
    """
    data: str = Field(
        ...,
        description="Text or audio file path",
        examples=["That phone's camera is great but the battery is terrible.", "/data/audio/customer_feedback_01.mp3"]
    )
    language: str = Field(
        "en", 
        description="The language of the content for analysis (e.g., 'tr', 'en').",
        examples=["tr", "en"]
    )