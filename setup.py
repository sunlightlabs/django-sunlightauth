#!/usr/bin/env python

from setuptools import setup, find_packages

from sunlightauth import __version__
LONG_DESCRIPTION = DESCRIPTION = "helper to login w/ sunlight auth"

setup(name='django-sunlightauth',
      version=__version__,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      author='James Turk',
      author_email='jturk@sunlightfoundation.com',
      url='http://github.com/sunlightlabs/django-sunlightauth',
      license="BSD License",
      platforms=["any"],
      install_requires=['django-social-auth'],
      packages=find_packages(),
     )
