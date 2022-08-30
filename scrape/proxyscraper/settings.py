
from __future__ import unicode_literals
import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")
import django
django.setup()

MEDIA_ALLOW_REDIRECTS = True


USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'

ITEM_PIPELINES = {
    'scrape.proxyscraper.pipelines.ProxyscraperPipeline': 300,
}

IMAGES_THUMBS = {
    'medium': (50, 50),
    'small': (25, 25),
}

SPIDER_MODULES = ['scrape.proxyscraper']

