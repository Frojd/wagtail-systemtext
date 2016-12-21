from django.conf import settings


SYSTEMTEXT_CACHE_PREFIX = getattr(settings, 'SYSTEMTEXT_CACHE_PREFIX',
                                  'wagtailsystemtext')
SYSTEMTEXT_CACHE_EXPIRY = getattr(settings, 'SYSTEMTEXT_CACHE_EXPIRY',
                                  600)  # 10 min
SYSTEMTEXT_REBUILD_ON_SAVE = getattr(settings, 'SYSTEMTEXT_REBUILD_ON_SAVE',
                                     True)
SYSTEMTEXT_USE_DEFAULT_ON_EMPTY = getattr(settings, 'SYSTEMTEXT_USE_DEFAULT_ON_EMPTY',
                                          False)
