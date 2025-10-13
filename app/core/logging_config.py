import logging
import os

from app.core.config import settings

def setup_logging():
    log_level = settings.LOG_LEVEL.upper()
    
    os.makedirs("logs", exist_ok=True)
    
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("logs/app.log", encoding="utf-8")
        ]
    )
    
    logger = logging.getLogger(__name__)
    logger.info(f"Logging initialized with level: {log_level}")
    return logger

logger = setup_logging()
