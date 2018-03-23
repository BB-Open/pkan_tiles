# -*- coding: utf-8 -*-
"""Validate the tile implementation."""

from collective.tiles.githubgist.testing import INTEGRATION_TESTING
from plone.testing.z2 import Browser
from urllib import quote

import unittest


class TestTile(unittest.TestCase):
    """Test that collective.tiles.githubgist is properly installed."""

    layer = INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.portalURL = self.portal.absolute_url()

        self.unprivileged_browser = Browser(self.layer['app'])

    def test_tile(self):
        """Validate the github gist tile."""
        tile_title = u'Sample Gist'
        gist_url = 'https://gist.github.com/user/gist_id'

        self.unprivileged_browser.open(
            self.portalURL +
            '/@@collective.tiles.githubgist/unique',
            data='gist_url=' + quote(gist_url) +
            '&tile_title=' + quote(tile_title) +
            '&show_title=1',
        )
        contents = self.unprivileged_browser.contents
        self.assertTrue(tile_title in contents)
        self.assertIn(
            '<script src="{0}.js">'.format(gist_url),
            self.unprivileged_browser.contents,
        )
