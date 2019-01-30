#!/usr/bin/env python

import sys

from django.conf import settings
from django.core.management import execute_from_command_line


if not settings.configured:
    params = dict(
        LOGGING={
            'version': 1,
            'disable_existing_loggers': False,
            'handlers': {
                'console': {
                    'class': 'logging.StreamHandler',
                },
            },
            'loggers': {
                'wagtailsystemtext': {
                    'handlers': ['console'],
                    'level': 'ERROR',
                    'propagate': True,
                },
            },
        },
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
            }
        },
        INSTALLED_APPS=[
            'django.contrib.contenttypes',
            'django.contrib.auth',
            'django.contrib.sites',
            'wagtail.core',
            'wagtail.sites',
            'wagtail.users',
            'wagtail.images',
            'taggit',
            'wagtailsystemtext',
            "tests",
        ],
        SYSTEMTEXT_CACHE_PREFIX='wagtailsystemtext_test',
        MIDDLEWARE=[],
        ROOT_URLCONF='tests.urls',
    )

    settings.configure(**params)


def runtests():
    argv = sys.argv[:1] + ["test"] + sys.argv[1:]
    execute_from_command_line(argv)


if __name__ == "__main__":
    runtests()
