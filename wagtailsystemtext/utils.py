try:
    from threading import local
except ImportError:
    from django.utils._threading_local import local

from django.core.cache import cache

from wagtailsystemtext import app_settings
from wagtailsystemtext.models import SystemString


_thread_locals = local()


def _cleanup():
    del _thread_locals.site
    del _thread_locals.index


def set_site(site):
    _thread_locals.site = site


def get_site():
    return _thread_locals.site


def in_cache(site):
    return cache_key(site) in cache


def cache_key(site):
    return '{}:{}'.format(app_settings.SYSTEMTEXT_CACHE_PREFIX, site.pk)


def get_from_cache(site):
    return cache.get(cache_key(site))


def fill_cache(site):
    string_qs = SystemString.objects.filter(site=site)
    strings = {u'{}:{}'.format(x.group, x.identifier): x.string
               for x in string_qs}

    cache.set(cache_key(site), strings, app_settings.SYSTEMTEXT_CACHE_EXPIRY)


def preload(site):
    index = get_index()
    strings = get_from_cache(site)
    index['site_{}'.format(site.pk)] = strings

    _thread_locals.index = index


def get_index():
    if not getattr(_thread_locals, 'index', None):
        return {}

    return _thread_locals.index


def current_strings():
    values = get_index()
    key = 'site_{}'.format(get_site().pk)

    if not key in values:
        return {}

    return values[key]


def gettext(identifier, group=SystemString.DEFAULT_GROUP):
    strings = current_strings()
    value = identifier
    key = u'{}:{}'.format(group, identifier)

    if key in strings:
        return strings[key]

    # TODO: Add detect new signal
    instance = SystemString.objects.get_or_create(
        identifier=identifier,
        group=group,
        site=get_site(),
    )

    return value
