"""
copyright bijan shokrollahi
03.17.2022

"""

import logging
from pathlib import Path
from definitions import ROOT_DIR


def setup_logging() -> None:
    # Logging setup
    logging_config = get_logging_config()
    console_handler = logging_config.get('handlers', {}).get('console')
    if console_handler is not None:
        console_handler['level'] = 'CRITICAL'
    file_handler = logging_config.get('handlers', {}).get('file')
    if file_handler is not None:
        Path(file_handler['filename']).parent.mkdir(parents=True, exist_ok=True)
    logging.config.dictConfig(logging_config)


def get_logging_config():
    # Default logging configuration - JSON formatted
    # Reason for setting level at chardet.charsetprober is to prevent unwanted debug messages from requests module
    logging_config = {
        "version": 1,
        "formatters": {
            "simple": {
                "format": "%(levelname)s: {%(module)s} [%(funcName)s] %(message)s"
            },
            "detailed": {
                "format": "%(asctime)s: %(name)s: %(levelname)s: {%(module)s} [%(funcName)s] %(message)s"
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "CRITICAL",
                "formatter": "simple"
            },
            "file": {
                "class": "logging.handlers.RotatingFileHandler",
                "filename": f"{ROOT_DIR}/logs/bitcoin_pricer.log",
                "backupCount": 3,
                "maxBytes": 2097152,
                "level": "DEBUG",
                "formatter": "detailed"
            }
        },
        "root": {
            "handlers": ["console", "file"],
            "level": "DEBUG"
        },
        "loggers": {
            "chardet.charsetprober": {
                "level": "INFO"
            },
            "aide.statistics": {
                "level": "WARN"
            }
        }
    }
    return logging_config
