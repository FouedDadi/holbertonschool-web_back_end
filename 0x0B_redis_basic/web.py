#!/usr/bin/env python3
"""[summary]"""

import requests


def get_page(url: str) -> str:
    """[summary]

    Args:
        url (str): [description]

    Returns:
        str: [description]
    """
    r = requests.get(url)
    return r.content
