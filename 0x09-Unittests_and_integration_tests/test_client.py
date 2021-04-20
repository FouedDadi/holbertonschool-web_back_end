#!/usr/bin/env python3
"""[summary]"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """[summary]

    Args:
        unittest ([type]): [description]
    """
    @parameterized.expand([
        ("google"),
        ("abc"),
        ])
    @patch('client.get_json')
    def test_org(self, orgs, mocker):
        """[summary]

        Args:
            orgs ([type]): [description]
            mocker ([type]): [description]

        Returns:
            [type]: [description]
        """
        clt = GithubOrgClient(orgs)
        self.assertEqual(clt.org, mocker.return_value)
