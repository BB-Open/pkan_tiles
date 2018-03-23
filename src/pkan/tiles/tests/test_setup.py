# -*- coding: utf-8 -*-
"""Test Setup of collective.tiles.githubgist."""

from collective.tiles.githubgist.config import PROJECT_NAME
from collective.tiles.githubgist.testing import INTEGRATION_TESTING
from plone import api
from plone.browserlayer.utils import registered_layers

import unittest


class TestSetup(unittest.TestCase):
    """Validate setup process for collective.tiles.githubgist."""

    layer = INTEGRATION_TESTING

    def setUp(self):
        """Additional test setup."""
        self.portal = self.layer['portal']

    def test_product_installed(self):
        """Validate that our product is installed."""
        qi = self.portal.portal_quickinstaller
        self.assertTrue(qi.isProductInstalled(PROJECT_NAME))

    def test_addon_layer(self):
        """Validate that the browserlayer for our product is installed."""
        from pkan.tiles.interfaces import (
            IPKANTilesLayer,
        )
        self.assertIn(IPKANTilesLayer, registered_layers())


class TestUninstall(unittest.TestCase):
    """Validate uninstall process for plonetheme.barcelonetang."""

    layer = INTEGRATION_TESTING

    def setUp(self):
        """Additional test setup."""
        self.portal = self.layer['portal']

        qi = self.portal.portal_quickinstaller
        with api.env.adopt_roles(['Manager']):
            qi.uninstallProducts(products=[PROJECT_NAME])

    def test_product_is_uninstalled(self):
        """Validate that our product is uninstalled."""
        qi = self.portal.portal_quickinstaller
        self.assertFalse(qi.isProductInstalled(PROJECT_NAME))

    def test_addon_layer_removed(self):
        """Validate that the browserlayer is removed."""
        from pkan.tiles.interfaces import (
            IPKANTilesLayer,
        )
        self.assertNotIn(IPKANTilesLayer, registered_layers())
