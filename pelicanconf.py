#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'skamath'
SITENAME = u"Sachin's Blog"
#SITEURL = 'localhost:8000'
PATH = 'content'
THEME = 'medius'
TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = u'en'
DISQUS_SITENAME='sachinwritesxyz'

# Feed generation is usually not desired when developing
DELETE_OUTPUT_DIRECTORY = False
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
CATEGORY_FEED_RSS = 'rss/%s.xml'
TAG_FEED_RSS = 'rss/tag-%s.xml'

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


MEDIUS_AUTHORS = {
    'skamath': {
        'description': """
            I am a self-proclaimed command-line warrior and web ninja, who slays the bad folks <i>(usually with a -9)</i>. I love security and forensics as much as I love Python. 
        """,
        'cover': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Milky_Way_Arch.jpg/1920px-Milky_Way_Arch.jpg',
        'image': 'https://lh6.googleusercontent.com/-zEMaXmWAhdI/AAAAAAAAAAI/AAAAAAAAAAA/eVdgsm3TIDU/s128-c-k/photo.jpg',
        'links': (('github', 'https://github.com/sachinkamath'),
                  ('envelope-square', 'mailto:sskamath96@gmail.com'),
                  ('twitter-square', 'https://twitter.com/iamskamath')),
    }
}
