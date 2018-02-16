import os.path
import unittest
from urllib.parse import urlparse

from mock import patch

from test.RestTest import ClientAPI


def fake_urlopen(url):
    """
    A stub urlopen() implementation that load json responses from
    the filesystem.
    """
    # Map path from url to a file
    parsed_url = urlparse(url)
    resource_file = os.path.normpath('tests/resources%s' % parsed_url.path)
    # Must return a file-like object
    return open(resource_file, mode='rb')


class ClientTestCase(unittest.TestCase):
    """Test case for the client methods."""

    def setUp(self):
        self.patcher = patch('RestTest.urlopen', fake_urlopen)
        self.patcher.start()
        self.client = ClientAPI()

    def tearDown(self):
        self.patcher.stop()

    def test_request(self):
        """Test a simple request."""
        user = 'sobkoNick'
        response = self.client.request(user)
        self.assertIn('name', response)
        self.assertEqual(response['name'], 'Mykola Sobko')
