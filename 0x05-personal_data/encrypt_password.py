#!/usr/bin/env python3
"""[crypting and decrypting password]"""
import bcrypt


def hash_password(password: str) -> bytes:
    """[generate a pasword hashign]

    Args:
        password (str): [description]

    Returns:
        bytes: [description]
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """[check if pwd is valid]

    Args:
        hashed_password (bytes): [description]
        password (str): [description]

    Returns:
        bool: [description]
    """
    return bcrypt.checkpw(password.encode(), hashed_password)
