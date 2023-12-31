#!/usr/bin/env python3

"""
Module for testing client.py
"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Testing GithubOrgClient class"""

    @parameterized.expand([
        "google",
        "abc"
    ])
    def test_org(self, org: str):
        """Testing with different inputs"""
        with patch("requests.get") as mock_get:
            mock_get.return_value.json.return_value = {"org": org}
            client_org = GithubOrgClient(org)
            self.assertEqual(client_org.org, {"org": org})

    @parameterized.expand([
        ("google", "google/repos"),
        ("abc", "error")
    ])
    def test_public_repos_url(self, org: str, url: str):
        """Testing public repos url"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": url}
            client_org = GithubOrgClient(org)
            self.assertEqual(client_org._public_repos_url, url)

    @patch("client.get_json")
    def test_public_repos(self, mock_get):
        """Testing public_repos"""
        mock_get.return_value = [{"name": "mostafa"}]

        with patch.object(GithubOrgClient,
                          "_public_repos_url",
                          new_callable=PropertyMock) as mock_public:
            payload = ["mostafa"]
            mock_public.return_value = payload
            client = GithubOrgClient("me")
            repos = client.public_repos()
            self.assertEqual(repos, payload)
            mock_get.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license, has_license):
        """Testing has license"""
        client = GithubOrgClient("google")
        self.assertEqual(client.has_license(repo, license), has_license)
