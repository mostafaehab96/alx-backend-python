#!/usr/bin/env python3

"""
Module for testing practices
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """Testing utils.access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_output):
        """Testing normal inputs"""
        self.assertEqual(access_nested_map(nested_map, path), expected_output)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Testing exception cases"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """A class for testing get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, test_payload):
        """Testing utils.get_json function"""

        with patch("requests.get") as mock_get:
            mock_get(url).json.return_value = test_payload
            mock_get.assert_called_once_with(url)
            result = get_json(url)
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Testing memoization"""

    @parameterized.expand([
        20, 30
    ])
    def test_memoize(self, input):
        """Test utils.memoize decorator"""

        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_a_method:
            test_class = TestClass()
            mock_a_method.return_value = input
            self.assertEqual(test_class.a_property, input)
            mock_a_method.assert_called_once()
