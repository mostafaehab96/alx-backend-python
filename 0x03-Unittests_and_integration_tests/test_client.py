#!/usr/bin/env python3

"""
Module for testing client.py
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Testing GithubOrgClient class"""

    @parameterized.expand([
        "google",
        "abc"
    ])
    def test_org(self, org):
        """Testing with different inputs"""
        with patch("requests.get") as mock_get:
            mock_get.return_value.json.return_value = {"org": org}
            client_org = GithubOrgClient(org)
            self.assertEqual(client_org.org, {"org": org})
