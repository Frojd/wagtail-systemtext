from django.core.management.base import BaseCommand
from wagtail.wagtailcore.models import Site

from wagtailsystemtext.models import SystemString


class Command(BaseCommand):
    """
    Sync system text to make sure all Wagtail sites contains the same text
    """
    def handle(self, *args, **options):
        strings = SystemString.objects.values_list('identifier', 'group')\
            .distinct()

        sites = Site.objects.all()
        for string in strings:
            identifier, group = string
            for site in sites:
                if SystemString.objects.filter(identifier=identifier,
                                               group=group,
                                               site=site).exists():
                    continue

                self.stdout.write(u'Syncing: {}:{} to {}'.format(identifier,
                                                                 group,
                                                                 site))
                SystemString.objects.create(
                    identifier=identifier,
                    group=group,
                    site=site,
                )

        self.stdout.write('Done!')
