from django.core.management.base import BaseCommand
from wagtail.wagtailcore.models import Site

from wagtailsystemtext.models import SystemString


class Command(BaseCommand):
    """
    Add system text to Wagtail websites
    """
    def add_arguments(self, parser):
        parser.add_argument('--identifier', required=True)
        parser.add_argument('--group', default=SystemString.DEFAULT_GROUP)
        parser.add_argument('--site_id', type=int, default=-1)

    def handle(self, *args, **options):
        identifier = options['identifier']
        group = options['group']
        site_id = options['site_id']

        sites = Site.objects.all()
        if site_id != -1:
            sites = sites.filter(pk=site_id)

        for site in sites:
            if SystemString.objects.filter(identifier=identifier,
                                           group=group,
                                           site=site).exists():

                self.stdout.write(u'{}:{} on {} already exist'.format(
                    identifier, group,
                    site))
                continue

            self.stdout.write(u'Adding: {}:{} to {}'.format(identifier, group,
                                                            site))
            SystemString.objects.create(
                identifier=identifier,
                group=group,
                site=site,
            )

        self.stdout.write('Done!')
