#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'NIDASH'
SITENAME = u'NIDASH Data Model'
SITEURL = ''

THEME = 'bootstrap2'

TIMEZONE = 'UTC'

DEFAULT_LANG = u'en'

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('INCF', 'http://incf.org'),
          ('NIDASH Wiki', 
          	'http://wiki-new.incf.org/mediawiki/index.php'
          	'/Neuroimaging_Task_Force'),)

# Social widget
SOCIAL = (('GitHub', 'http://github.com/ni-'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
