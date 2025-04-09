# import logging
# import os

# def setup_logger(name, log_dir='logs', level=logging.INFO):
#     """
#     Set up a logger with the specified name and logging level.
#     Logs are saved in the specified directory.
#     """
#     if not os.path.exists(log_dir):
#         os.makedirs(log_dir)
    
#     log_file = os.path.join(log_dir, f'{name}.log')
    
#     logger = logging.getLogger(name)
#     logger.setLevel(level)
    
#     # File handler
#     file_handler = logging.FileHandler(log_file)
#     file_handler.setLevel(level)
    
#     # Console handler
#     console_handler = logging.StreamHandler()
#     console_handler.setLevel(level)
    
#     # Formatter
#     formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#     file_handler.setFormatter(formatter)
#     console_handler.setFormatter(formatter)
    
#     # Add handlers to the logger
#     logger.addHandler(file_handler)
#     logger.addHandler(console_handler)
    
#     return logger


import logging
import os
from pathlib import Path

LOG_DIR = Path(__file__).parent.parent.parent / "logs"
LOG_DIR.mkdir(exist_ok=True)

def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.DEBUG)

    log_file = LOG_DIR / f"{name}.log"
    fh = logging.FileHandler(log_file, mode='a')
    fh.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s: %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger
