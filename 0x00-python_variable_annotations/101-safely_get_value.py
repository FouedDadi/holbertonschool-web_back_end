#!/usr/bin/env python3
"""[annotate a function]"""
from typing import TypeVar, Union, Any, Mapping

T = TypeVar("T")


def safely_get_value(dct: Mapping,
                    key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """[summary]

    Args:
        dct (Mapping): [arg 1]
        key (Any): [key]
        default (Union[T, None], optional):
        [union of T and None]. Defaults to None.

    Returns:
        Union[Any, T]: [union of Any and T]
    """
    if key in dct:
        return dct[key]
    else:
        return default
