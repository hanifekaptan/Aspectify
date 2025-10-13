from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.tools import tool

from app.schemas.response.llm_response import LLMResponse
from app.ai_models.llm_models import gemini_2_5_pro

parser = JsonOutputParser(pydantic_object=LLMResponse)

template = """
Your task is to perform aspect-based sentiment analysis on the given text and provide a sentiment analysis for each aspect separately.
Return the result as a JSON object, including the aspect, sentiment, score, and the exact quote from the text for each aspect.
Return the result in the specified language.

EXAMPLE:
Text: "The screen of this phone has vibrant colors, but the battery life disappointed me."
Output:
{{
    "polarity": "positive",
    "score": 0.95,
    "aspects": [
        {{
            "aspect": "screen",
            "sentiment": "positive",
            "score": 0.95,
            "quote": "screen is amazing, colors are very vibrant"
        }},
        {{
            "aspect": "battery life",
            "sentiment": "negative",
            "score": 0.98,
            "quote": "battery barely lasts a day"
        }}
    ]
}}

{format_instructions}

Now, analyze the given text:
Text: "{text}"
Language: "{language}"
"""

prompt = ChatPromptTemplate.from_template(
    template=template,
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

chain = prompt | gemini_2_5_pro | parser

@tool
def absa_analyzer_tool(text: str, language: str = "tr") -> dict:
    """
    Performs aspect-based sentiment analysis on the given text.
    
    Args:
        text (str): The text to analyze for sentiment aspects
        language (str): The language of the text (default: "tr")
    
    Returns:
        dict: Dictionary containing polarity, score, and aspects with their sentiments
    """
    return chain.invoke({"text": text, "language": language})