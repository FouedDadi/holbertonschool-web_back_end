#!/usr/bin/env python3
"""[BasicAuth class]"""
from api.v1.auth.auth import Auth
from flask import request
from typing import TypeVar, List
import base64


class BasicAuth(Auth):
    """[summary]

    Args:
        Auth ([type]): [description]
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """[summary]

        Args:
            authorization_header (str): [description]

        Returns:
            str: [description]
        """
        if authorization_header is None:
            return None
        if type(authorization_header) != str:
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split(' ')[1]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                               str) -> str:
        """[summary]

        Args:
            base64_authorization_header (str): [description]

        Returns:
            str: [description]
        """
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) != str:
            return None
        try:
            encoded = base64_authorization_header.encode('utf-8')
            decoded = base64.b64decode(encoded)
            value = decoded.decode('utf-8')
            return value
        except Exception:
            return None
