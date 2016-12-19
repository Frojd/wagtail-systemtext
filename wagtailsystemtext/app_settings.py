from django.conf import settings


SYSTEMTEXT_CACHE_PREFIX = getattr(settings, 'SYSTEMTEXT_CACHE_PREFIX',
                                  'wagtailsystemtext')
SYSTEMTEXT_CACHE_EXPIRY = getattr(settings, 'SYSTEMTEXT_CACHE_EXPIRY', 60)
