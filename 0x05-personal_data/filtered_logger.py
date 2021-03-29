#!/usr/bin/env python3
"""[contains different function]"""
import re
from typing import List
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """[initialisation]

        Args:
            fields (List[str]): [description]
        """
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """[updating format]

        Args:
            record (logging.LogRecord): [description]

        Returns:
            str: [description]
        """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """[function filter_datum that returns the log message obfuscated]

    Args:
        fields (List[str]): [description]
        redaction (str): [description]
        message (str): [description]
        separator (str): [description]

    Returns:
        str: [description]
    """
    for field in fields:
        message = re.sub(rf'{field}=.*?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message

def get_logger() -> logging.Logger:
    """[summary]

    Returns:
        logging.Logger: [description]
    """
    