"""
Module for microservice logging
"""

import os
import logging

import pythonjsonlogger.jsonlogger


def getLogger(name, level="WARNING", root_level=True):
    """
    Gets the logger with a name and sets for all
    """

    level = os.environ.get("LOG_LEVEL", level)

    handler = logging.StreamHandler()
    handler.setFormatter(pythonjsonlogger.jsonlogger.JsonFormatter(
        fmt="%(created)f %(asctime)s %(name)s %(levelname)s %(pathname)s %(funcName)s %(lineno)d %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S %Z"
    ))

    root = logging.getLogger()
    root.handlers = []
    root.addHandler(handler)

    if root_level:
        root.setLevel(level)

    custom = logging.getLogger(name)
    custom.setLevel(level)

    return custom
