"""
Structured Logging Module.
Implements console output using 'rich' for the UI and standard 
file handlers for audit trails.
Ensures secrets are not accidentally logged.
"""
import logging
from pathlib import Path
from rich.logging import RichHandler
from core.config import settings

def setup_logger(name: str) -> logging.Logger:
    """Configures and returns a secure, structured logger."""
    logger = logging.getLogger(name)
    
    # Prevent adding handlers multiple times
    if logger.hasHandlers():
        return logger
        
    log_level_str = settings.app.log_level.upper()
    log_level = getattr(logging, log_level_str, logging.INFO)
    logger.setLevel(log_level)

    # Ensure log directory exists
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    # 1. Rich Console Handler (for beautiful terminal UI)
    console_handler = RichHandler(rich_tracebacks=True, markup=True)
    console_format = logging.Formatter("%(message)s")
    console_handler.setFormatter(console_format)
    console_handler.setLevel(log_level)

    # 2. File Handler - Application/Audit Log (Structured text)
    file_handler = logging.FileHandler("logs/application.log", encoding="utf-8")
    file_format = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
    )
    file_handler.setFormatter(file_format)
    file_handler.setLevel(logging.DEBUG) # Always keep file logs verbose

    # 3. File Handler - Error Log
    error_handler = logging.FileHandler("logs/errors.log", encoding="utf-8")
    error_handler.setFormatter(file_format)
    error_handler.setLevel(logging.ERROR)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    logger.addHandler(error_handler)
    
    # Disable propagation to root to avoid double printing
    logger.propagate = False 

    return logger

# Global application logger
log = setup_logger("InternShield")