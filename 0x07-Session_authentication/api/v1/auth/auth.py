#!/usr/bin/env python3
"""[auth]"""
from flask import request
from typing import TypeVar, List
from os import getenv


class Auth:
    """[summary]
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """[summary]
        Args:
            path (str): [description]
            excluded_paths (List[str]): [description]

        Returns:
            bool: [description]
        """
        if path is None:
            return True
        if excluded_paths is None or excluded_paths == []:
            return True
        if path[-1] != "/":
            path += "/"
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """[summary]

        Args:
            request ([type], optional): [description]. Defaults to None.

        Returns:
            str: [description]
        """
        if request is None:
            return None
        if "Authorization" not in request.headers:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """[summary]

        Returns:
            [type]: [description]
        """
        return None

    def session_cookie(self, request=None):
        """[summary]

        Args:
            request ([type], optional): [description]. Defaults to None.
        """
        if request is None:
            return None
        return request.cookies.get(getenv("SESSION_NAME"))
