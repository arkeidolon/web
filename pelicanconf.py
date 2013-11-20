#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Steve'
SITENAME = u'Python Philippines'
SITEURL = 'http://localhost:8000'

TIMEZONE = 'Asia/Manila'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# # Blogroll
# LINKS = (
#   ('Pelican', 'http://getpelican.com/'),
#   ('Python.org', 'http://python.org/'),
#   ('Jinja2', 'http://jinja.pocoo.org/'),
# )

# # Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

THEME = 'themes/mabuhay'

MENUITEMS = (
  ('Home', '/'),
  ('Meetups', 'http://meetups.python.ph'),
  ('Blog', 'http://blog.python.ph'),
)

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
