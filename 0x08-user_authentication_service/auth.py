#!/usr/bin/env python3
"""[summary]"""
import bcrypt


def _hash_password(password: str) -> str:
    """[summary]

    Args:
        password (str): [description]

    Returns:
        str: [description]
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
