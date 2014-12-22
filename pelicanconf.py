#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Michael Wessler'
SITENAME = u'Michael Wessler'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


#User-Added
THEME = '../pelican-bootstrap3/'
STATIC_PATHS = ['images']

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

#SITE_LOGO = 'images/psu.gif'
#BANNER = '/path/to/banner.png'
#BANNER_SUBTITLE = 'This is my subtitle'
#BANNER_ALL_PAGES = True

#INDEX_SAVE_AS = '/pages/about.html'
INDEX_SAVE_AS = 'blog_index.html'
MENUITEMS = (('Blog','/blog_index.html'),('Research','/pages/research.html'),('Resume','/pages/resume.html'),('About','/pages/about.html'))

TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''
DISPLAY_TAGS_ON_SIDEBAR = False
HIDE_SIDEBAR = True

# Blogroll
#LINKS = ()

# Social widget
#SOCIAL = ()

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
