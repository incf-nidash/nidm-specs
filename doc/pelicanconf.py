#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'NIDM Working Group'
SITENAME = u'Neuroimaging Data Model'
SITEURL = ''

THEME = 'pelican-bootstrap3'
BOOTSTRAP_THEME = 'readable'

TIMEZONE = 'UTC'

PATH = "content"

DEFAULT_LANG = u'en'

STATIC_PATHS = ['images', 'specs', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('INCF', 'http://incf.org'),
          ('NIDASH Wiki', 'http://wiki.incf.org/mediawiki/index.php/Neuroimaging_Task_Force'),)

# Social widget
SOCIAL = (('github', 'http://github.com/incf-nidash'),)

# AddThis Pro
ADDTHIS_PROFILE = 'ra-52e5a80938eff3d6'

# GitHub widget
GITHUB_USER = 'incf-nidash'
GITHUB_REPO_COUNT = 3
GITHUB_SKIP_FORK = True
GITHUB_SHOW_USER_LINK = True

# Side panel menu
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
TAG_CLOUD_MAX_ITEMS = 25
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
RECENT_POST_COUNT = 5

DEFAULT_PAGINATION = 10

READERS = {'html': None}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
