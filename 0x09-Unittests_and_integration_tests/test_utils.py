#!/usr/bin/env python3
"""[summary]"""
import unittest
from mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """[summary]

    Args:
        unittest ([type]): [description]
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """[summary]

        Args:
            map ([type]): [description]
            path ([type]): [description]
            output ([type]): [description]
        """
        output = access_nested_map(map, path)
        self.assertEqual(output, expected)
