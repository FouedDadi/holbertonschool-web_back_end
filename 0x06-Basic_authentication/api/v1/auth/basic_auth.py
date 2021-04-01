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
