#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Scott M. Koch'
SITENAME = u'Scott Koch'
SITEURL = 'http://www.scott-koch.com'

PATH = 'content'

TIMEZONE = 'America/New_York'
THEME = 'pelican-bootstrap3'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
LOAD_CONTENT_CACHE = False

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (('Blog', 'blog.html'),)
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'misc'

# Blogroll
LINKS = (('github', 'http://github.com/scootersmk'),
         ('stack-overflow', 'http://stackoverflow.com/users/8485643/scott-koch'),)

# Social widget
SOCIAL = (('facebook', 'https://www.facebook.com/scottmkoch'),
          ('linkedin', 'http://linkedin.com/in/scottkoch'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ["plugins", "/home/koch/Git/pelican-plugins"]
PLUGINS = ['i18n_subsites']
BOOTSTRAP_THEME = 'yeti'
BOOTSTRAP_NAVBAR_INVERSE = True

DISPLAY_CATEGORY = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True

INDEX_SAVE_AS = 'blog.html'

STATIC_PATHS = ['images', 'extra/robots.txt', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}
