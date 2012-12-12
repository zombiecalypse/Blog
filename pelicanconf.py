#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Zombiecalypse'
AUTHOR_EMAIL = 'maergil@gmail.com'
SITENAME = u'Zombiecalypse the Blog'
SITEURL = 'http://zombiecalypse.github.com/Blog'
STATIC_PATHS = [ 'images' ]
ARTICLE_URL = '{date:%Y}/{date:%b}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%b}/{slug}.html'

TYPOGRIFY = True

RELATIVE_URLS = True

TIMEZONE = 'Europe/Zurich'

DEFAULT_LANG = u'en'

# Blogroll
LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
          ('Python.org', 'http://python.org'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/zombiecalypse'),
          ('github', 'http://github.com/zombiecalypse'),)

PLUGINS = ['pelican.plugins.gravatar',]

DEFAULT_PAGINATION = 10
