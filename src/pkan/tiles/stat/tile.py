# -*- coding: utf-8 -*-
"""Tile implementation."""
from collections import OrderedDict
from pkan.dcatapde.constants import DCAT_CTs
from pkan.dcatapde.i18n import CT_DCAT_CATALOG
from pkan.dcatapde.i18n import CT_DCAT_DATASET
from pkan.dcatapde.i18n import CT_DCAT_DISTRIBUTION
from pkan.dcatapde.i18n import CT_LABELS
from pkan.dcatapde.i18n import LABEL_DCAT_CATALOG
from pkan.dcatapde.i18n import LABEL_DCAT_DATASET
from pkan.dcatapde.i18n import LABEL_DCAT_DISTRIBUTION
from pkan.tiles import _
from plone import api
from plone import tiles
from plone.app.standardtiles import _PMF
from plone.i18n.normalizer.interfaces import IIDNormalizer
from plone.supermodel.model import Schema
from zope import schema
from zope.component import queryUtility


class IPKANStatTile(Schema):
    """A tile that shows Gists from GitHub."""

    tile_title = schema.TextLine(
        description=_PMF(
            u'The title will also be used to create identifying class on '
            u'that tile',
        ),
        required=True,
        title=_PMF(u'Title'),
    )

    show_title = schema.Bool(
        default=True,
        title=_PMF(u'Show tile title'),
    )

    title_level = schema.Choice(
        default=u'h2',
        required=False,
        title=_(u'Headline level'),
        values=(u'h1', u'h2', u'h3', u'h4', u'h5', u'h6'),
    )


STAT_TYPES = OrderedDict()
STAT_TYPES[CT_DCAT_CATALOG] = LABEL_DCAT_CATALOG
STAT_TYPES[CT_DCAT_DATASET] = LABEL_DCAT_DATASET
STAT_TYPES[CT_DCAT_DISTRIBUTION] = LABEL_DCAT_DISTRIBUTION


class PKANStatTile(tiles.Tile):
    """A tile that shows PKAN Statistics."""

    @property
    def tile_id(self):
        return queryUtility(IIDNormalizer).normalize(
            self.data.get('tile_title'),
        )

    @property
    def tile_title(self):
        return self.data.get('tile_title')

    @property
    def show_title(self):
        return self.data.get('show_title')

    @property
    def title_level(self):
        return self.data.get('title_level') or u'h2'

    def stat(self):
        catalog = api.portal.get_tool('portal_catalog')
        for portal_type in DCAT_CTs:
            results = catalog.searchResults(**{'portal_type': portal_type})
            yield {
                'portal_type': portal_type,
                'label': CT_LABELS[portal_type],
                'results': results,
            }

    def stat_count(self):
        for entry in self.stat():
            yield {
                'label': entry['label'],
                'count': len(entry['results']),
            }
