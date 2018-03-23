# -*- coding: utf-8 -*-
"""Setup for pkan.tiles package."""

from setuptools import (
    find_packages,
    setup,
)

version = '0.1'
description = "A tile that shows PKAN content"
long_description = ('\n'.join([
    open('README.rst').read(),
    'Contributors',
    '------------\n',
    open('CONTRIBUTORS.rst').read(),
    open('CHANGES.rst').read(),
]))


install_requires = [
    'setuptools',
    # -*- Extra requirements: -*-
    'plone.api',
    'plone.app.standardtiles',
    'plone.app.tiles',
    'plone.i18n',
    'plone.supermodel',
    'plone.tiles',
    'pygments',
    'zope.component',
    'zope.schema',
]

setup(
    name='pkan.tiles',
    version=version,
    description=description,
    long_description=long_description,
    # Get more from https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone",
        "Framework :: Plone :: 5.0",
        "Framework :: Plone :: 5.1",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ],
    keywords='Python Plone PKAN',
    author='inqbus',
    author_email='volker.jaenisch@inqbus.de',
    url='https://github.com/BB-Open/pkan.tiles',
    download_url='https://pypi.python.org/pypi/pkan.tiles',
    license='GPL version 2',
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'': 'src'},
    namespace_packages=['pkan'],
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    extras_require={
        'test': [
            'plone.app.mosaic',
            'plone.app.robotframework[debug]',
            'plone.app.testing',
            'robotframework-selenium2screenshots',
        ],
    },
    entry_points="""
    # -*- Entry points: -*-

    [z3c.autoinclude.plugin]
    target = plone
    """,
)
