#!/usr/bin/env python3
"""[contains different function]"""
import re
from typing import List
import logging
import os
import mysql.connector
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


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
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

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
    """[get logger]

    Returns:
        logging.Logger: [description]
    """
    log = logging.getLogger("user_data")
    log.propagate = False
    log.setLevel(logging.INFO)
    hand = logging.StreamHandler()
    hand.setFormatter(RedactingFormatter(PII_FIELDS))
    log.addHandler(hand)
    return log


def get_db() -> mysql.connector.connection.MySQLConnection:
    """[summary]

    Returns:
        mysql.connector.connection.MySQLConnection: [description]
    """
    connection = mysql.connector.connect(
                  usr=os.environ.get('PERSONAL_DATA_DB_USERNAME', 'root'),
                  pwd=os.environ.get('PERSONAL_DATA_DB_PASSWORD', ''),
                  host=os.environ.get('PERSONAL_DATA_DB_HOST', 'localhost'),
                  db=os.environ.get('PERSONAL_DATA_DB_NAME', ''))
    return connection
