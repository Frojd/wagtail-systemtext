from django.utils.deprecation import MiddlewareMixin

from wagtailsystemtext.utils import (
    in_cache,
    fill_cache,
    set_site,
    preload,
)


class SiteSystemTextMiddleware(MiddlewareMixin):
    def process_request(self, request):
        site = request.site

        set_site(request.site)

        if not in_cache(site):
            fill_cache(site)

        preload(site)
