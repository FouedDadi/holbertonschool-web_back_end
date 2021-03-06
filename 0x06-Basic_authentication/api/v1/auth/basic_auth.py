#!/usr/bin/env python3
"""[BasicAuth class]"""
from api.v1.auth.auth import Auth
from flask import request
from typing import TypeVar, List
import base64
from models.user import User


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

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                     str) -> (str, str):
        """[summary]

        Args:
            self ([type]): [description]
            str ([type]): [description]
        """
        if decoded_base64_authorization_header is None:
            return (None, None)
        if type(decoded_base64_authorization_header) != str:
            return (None, None)
        if ":" not in decoded_base64_authorization_header:
            return (None, None)
        email = decoded_base64_authorization_header.split(":", 1)[0]
        password = decoded_base64_authorization_header.split(":", 1)[1]
        return (email, password)

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """[summary]

        Args:
            self ([type]): [description]
        """
        if user_email is None or type(user_email) != str:
            return None
        if user_pwd is None or type(user_pwd) != str:
            return None
        try:
            credentials = User.search({"email": user_email})
            if not credentials:
                return None
        except Exception:
            return None
        for pair in credentials:
            if not pair.is_valid_password(user_pwd):
                return None
            else:
                return pair

    def current_user(self, request=None) -> TypeVar('User'):
        """[summary]
        """
        head = self.authorization_header(request)
        b64_head = self.extract_base64_authorization_header(head)
        decode = self.decode_base64_authorization_header(b64_head)
        credentials = self.extract_user_credentials(decode)
        return self.user_object_from_credentials(credentials[0],
                                                 credentials[1])
