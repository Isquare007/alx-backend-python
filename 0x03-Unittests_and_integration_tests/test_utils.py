#!/usr/bin/env python3
"""Create a TestAccessNestedMap class that
inherits from unittest.TestCase"""
from parameterized import parameterized
from unittest.mock import patch, Mock
from unittest import TestCase, mock
import unittest


from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        self.assertEqual(access_nested_map(nested_map, path), expected_result)
        
    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1,}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_result):
        """ Test that a KeyError is raised for the respective inputs """
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual(f"KeyError('{expected_result}')", repr(e.exception))
        
class TestGetJson(unittest.TestCase):
    """method to test that utils.get_json returns the expected result."""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)
        
class TestClass:
    def a_method(self):
        return 42

    @memoize
    def a_property(self):
        return self.a_method()

class TestMemoize(TestCase):
    def test_memoize(self):
        with mock.patch.object(TestClass, 'a_method') as mock_method:
            instance = TestClass()
            mock_method.return_value = 42
            result1 = instance.a_property
            result2 = instance.a_property
            mock_method.assert_called_once()
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)