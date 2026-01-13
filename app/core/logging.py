import logging
import sys


def setup_logger(name: str = "vis4ml", log_level: str = "INFO") -> logging.Logger:
    """
    Setup and configure application logger.

    Args:
        name: Logger name
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)

    Returns:
        configured logger instance
    """
    logger = logging.getLogger(name)
    level = getattr(logging, log_level.upper(), logging.INFO)
    logger.setLevel(level)

    # create console handler
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(level)

    # create formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    handler.setFormatter(formatter)

    # add handler to logger if not already added
    if not logger.handlers:
        logger.addHandler(handler)

    return logger


# initialize logger with default settings
# will be reconfigured in main.py with config settings
logger = setup_logger()
