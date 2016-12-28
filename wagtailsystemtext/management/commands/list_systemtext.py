from django.core.management.base import BaseCommand
from wagtail.wagtailcore.models import Site

from wagtailsystemtext.models import SystemString


class Command(BaseCommand):
    """
    List system text from Wagtail websites
    """
    def add_arguments(self, parser):
        parser.add_argument('--sort_field', default='identifier')
        parser.add_argument('--site_id', type=int, default=-1)

    def handle(self, *args, **options):
        sort_field = options['sort_field']
        site_id = options['site_id']

        sites = Site.objects.all()
        if site_id != -1:
            sites = sites.filter(pk=site_id)

        strings = SystemString.objects.filter(site__in=sites)\
            .order_by(sort_field)

        for string in strings:
            self.stdout.write(u'{}:{} on {}'.format(string.identifier,
                                                    string.group,
                                                    string.site))
