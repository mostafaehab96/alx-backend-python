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

    def test_memoize(self):
        """Test utils.memoize decorator"""

        class TestClass:
            """Test class"""

            def a_method(self):
                """Test method"""
                return 42

            @memoize
            def a_property(self):
                """Test property"""
                return self.a_method()

        with (patch.object(TestClass, 'a_method', return_value=42) as
              mock_a_method):
            test_class = TestClass()
            first = test_class.a_property
            second = test_class.a_property
            self.assertEqual(first, 42)
            self.assertEqual(second, 42)
            mock_a_method.assert_called_once()
