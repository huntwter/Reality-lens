import logging
import sys
from app.core.config import settings

def setup_logging():
    """
    Configures the application logger with a structured format.
    """
    logger = logging.getLogger("realitylens")
    logger.setLevel(logging.INFO if not settings.DEBUG else logging.DEBUG)
    
    # Console Handler
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    
    if not logger.handlers:
        logger.addHandler(handler)
        
    return logger

logger = setup_logging()
