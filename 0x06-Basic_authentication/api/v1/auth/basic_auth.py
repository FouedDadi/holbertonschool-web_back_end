#!/usr/bin/env python3
"""[BasicAuth class]"""
from api.v1.auth.auth import Auth
from flask import request
from typing import TypeVar, List


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
