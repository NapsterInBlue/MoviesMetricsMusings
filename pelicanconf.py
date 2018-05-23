#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Nick'
SITENAME = 'Movies, Metrics, Musings'
SITEURL = ''
PATH = 'content'
TIMEZONE = 'America/Detroit'
DEFAULT_LANG = 'English'
DEFAULT_DATE = 'fs'


STATIC_PATHS = ['images', 'favicon.ico', 'workspace', '.nojekyll']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Set the article URL
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

SUMMARY_MAX_LENGTH = 100
DEFAULT_PAGINATION = 10

THEME = 'theme'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

ABOUT_PAGE = '/pages/about.html'
TWITTER_USERNAME = 'NapsterInBlue'
GITHUB_USERNAME = 'NapsterInBlue'
LINKEDIN_PAGE = 'https://www.linkedin.com/in/nick-h-560001141/'

# Social widget
SOCIAL = (('Movie Reviews', 'https://letterboxd.com/nick_m3blog/films/reviews/'),
          ('Another social link', '#'),)


# Configuring Plugins and Notebook compatibility
MARKUP = ['md']
PLUGIN_PATHS = ['./plugins', './plugins/my-toc', './plugins/pelican-plugins', ]
PLUGINS = [
    'summary',       # auto-summarizing articles
    'feed_summary',  # use summaries for RSS, not full articles
    'ipynb.liquid',  # for embedding notebooks
    'liquid_tags.img',  # embedding images
    'liquid_tags.video',  # embedding videos
    'liquid_tags.youtube',
    'liquid_tags.include_code',  # including code blocks
    'liquid_tags.literal',
    'my-toc',           # Custom fork of pelican-toc
]

CODE_DIR = 'workspace/code'
NOTEBOOK_DIR = 'workspace/notebooks'

# Don't want to render temp files
IGNORE_FILES = ['.ipynb_checkpoints']

SHOW_ARCHIVES = True
ARCHIVES_PAGE = '/pages/archives.html'
SHOW_RESOURCES = True
RESOURCES_PAGE = '/pages/resources.html'
SHOW_NOTES = True
NOTES_PAGE = '/notes/'

MARKDOWN = {
    'extension_configs': {
         'markdown.extensions.toc': {'permalink': ' ',
                                     'anchorlink': False}
    }
}

TOC = {'TOC_HEADERS' : '^h[1-6]',
       'TOC_INCLUDE_TITLE': 'False'}
