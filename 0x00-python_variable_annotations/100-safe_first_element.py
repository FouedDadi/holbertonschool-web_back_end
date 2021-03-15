#!/usr/bin/env python3
"""[annotate a function]"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[any]) -> Union[Any, None]:
    """[Duck-type]

    Args:
        lst (Sequence[any]): [argument 1 of any]

    Returns:
        Union[any, None]: [any or none]
    """
    if lst:
        return lst[0]
    else:
        return None
