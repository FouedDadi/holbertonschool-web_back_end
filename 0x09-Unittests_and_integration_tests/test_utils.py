#!/usr/bin/env python3
"""[summary]"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


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
        output = access_nested_map(nested_map, path)
        self.assertEqual(output, expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, false_out):
        """[summary]

        Args:
            map ([type]): [description]
            path ([type]): [description]
            wrong_output ([type]): [description]
        """
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
            self.assertEquals(false_out, error.exception)


class TestGetJson(unittest.TestCase):
    """[summary]

    Args:
        unittest ([type]): [description]
    """
    @parameterized.expand([
       ("http://example.com", {"payload": True}),
       ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """[summary]

        Args:
            test_url ([type]): [description]
            test_payload ([type]): [description]
            mock_get ([type]): [description]
        """
        with patch('utils.requests.get') as mocker:
            mocker.return_value.json.return_value = test_payload
            res = get_json(test_url)
            self.assertEqual(res, test_payload)


class TestMemoize(unittest.TestCase):
    """[summary]

    Args:
        unittest ([type]): [description]
    """
    def test_memoize(self):
        """[summary]
        """
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, "a_method") as mocky:
            TestClass().a_property
            TestClass().a_property
