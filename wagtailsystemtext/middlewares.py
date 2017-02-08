import logging

from django.utils.deprecation import MiddlewareMixin

from wagtailsystemtext.utils import (
    in_cache,
    fill_cache,
    set_site,
    preload,
)


logger = logging.getLogger(__name__)


class SiteSystemTextMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if not hasattr(request, 'site'):
            logger.error('Request is missing site instance, have you added '
                         'wagtail.wagtailcore.middleware.SiteMiddleware '
                         'to your middleware classes?')

        site = request.site

        if not site:
            logger.error('Site is None on middleware request')
            return

        set_site(request.site)

        if not in_cache(site):
            fill_cache(site)

        preload(site)
