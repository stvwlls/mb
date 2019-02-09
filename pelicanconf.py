#!/usr/bin/env python
# -*- coding: utf-8 -*- #


AUTHOR = 'Mindful Building'
SITENAME = 'Mindful Building'
SITEURL = ''
THEME = 'themes/mb'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

DEFAULT_DATE = 'fs'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

FILENAME_METADATA = '(?P<slug>.*)_(?P<date>\d{4}-\d{2}-\d{2})'
STATIC_PATHS = ['images', 'extra/favicon.ico', 'css/fonts']
EXTRA_PATH_METADATA = {
        'extra/favicon.ico': {'path': 'favicon.ico'},
        }

DIRECT_TEMPLATES = ['index', 'categories', 'tags']

# Paths
INDEX_URL = 'projects'
INDEX_SAVE_AS = 'projects/index.html'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
#CATEGORY_URL = '{slug}'
#CATEGORY_SAVE_AS = '{slug}/index.html'
AUTHOR_SAVE_AS = ''
ARTICLE_ORDER_BY = 'basename'

# Processing
LOAD_CONTENT_CACHE = False 
TYPOGRIFY = True

# Menu
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

# Plugins
PLUGIN_PATHS = ['plugins']
#PLUGINS = ['thumbnailer','assets','neighbors','gzip_cache','optimize_images','gallery']
PLUGINS = ['thumbnailer','assets','neighbors','gzip_cache','photos']

#Photos
PHOTO_LIBRARY = "~/web/images/mb"
#	Absolute path to the folder where the original photos are kept, organized in sub-folders.

PHOTO_GALLERY = (1024, 768, 80)
#	For photos in galleries, maximum width and height, plus JPEG quality as a percentage. This would typically be the size of the photo displayed when the reader clicks a thumbnail.

PHOTO_ARTICLE = (500, 500, 70)
#	For photos associated with articles, maximum width, height, and quality. The maximum size would typically depend on the needs of the theme. 760px is suitable for the theme `notmyidea`.

PHOTO_THUMB = (280, 280, 70)
#	For thumbnails, maximum width, height, and quality.

PHOTO_SQUARE_THUMB = True
#	Crops thumbnails to make them square.

PHOTO_RESIZE_JOBS = 5
# Number of parallel resize jobs to be run. Defaults to 1.

#GALLERY_PATH = 'images/projects'

# Thumbnailer (wxh, wx?, ?xh, s(w=h))

#IMAGE_PATH = 'images/projects'
#THUMBNAIL_DIR = 'images/projects'
#THUMBNAIL_KEEP_TREE = True
#THUMBNAIL_KEEP_NAME = True
#THUMBNAIL_SIZES = {
#    #'sm': '400x400',
#    'medium': '300x?',
#}

#IMAGE_PATH = 'images/mastheads/interior'
#THUMBNAIL_DIR = 'images/mastheads'
#THUMBNAIL_SIZES = {
#    'mh-sm': '500x400',
#    'mh-md': '1000x500',
#    'mh-lg': '2000x450',
#}

#IMAGE_PATH = 'images/mastheads/home'
#THUMBNAIL_DIR = 'images/mastheads'
#THUMBNAIL_SIZES = {
#    'mh-sm': '500x400',
#    'mh-md': '1000x600',
#    'mh-lg': '2000x600',
#}

