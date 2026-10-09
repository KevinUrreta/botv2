import logging
from pathlib import Path

from src.core.config import settings

formatter = logging.Formatter(
    fmt="[%(asctime)s] [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

log_path = Path(settings.log_file)
log_path.parent.mkdir(parents=True, exist_ok=True)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

file_handler = logging.FileHandler(log_path, encoding="utf-8")
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

logger = logging.getLogger("discord")
logger.setLevel(logging.INFO)

if not logger.handlers:
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)

root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)

if not root_logger.handlers:
    root_logger.addHandler(stream_handler)
    root_logger.addHandler(file_handler)