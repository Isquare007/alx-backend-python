#!/usr/bin/env python3
"""Create a TestAccessNestedMap class that
inherits from unittest.TestCase"""
from parameterized import parameterized
import unittest


from utils import access_nested_map


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