import re
import os
import logging

from django.core.management.base import BaseCommand
from wagtail.wagtailcore.models import Site

from wagtailsystemtext.models import SystemString


logger = logging.getLogger(__name__)


API_PTRNS = (
    re.compile("_st\((.*?)\)"),
    re.compile("systemtext\((.*?)\)"),
)

TMPL_PTRNS = re.compile("{%.systemtext(.*)%}")


def get_files(path):
    matched_files = []

    for root, dirs, files in os.walk(path):
        for file_ in files:
            if file_.endswith('.py'):
                matched_files.append(os.path.join(root, file_))
            if file_.endswith('.html'):
                matched_files.append(os.path.join(root, file_))

    return matched_files


def parse_api(result):
    if not result:
        return None

    value = result.group(1)
    value = value.replace("'", "")
    value = value.replace("\"", "")
    value = value.split(",")
    value = [x.strip() for x in value]
    value = value[:2]

    if len(value) == 1:
        value.append(SystemString.DEFAULT_GROUP)

    identifier = value[0]
    group = value[1]

    if not re.search('^\w*$', identifier) or not \
            re.search('^\w*$', group):
        return None

    return (identifier, group)


def parse_tmpl(result):
    if not result:
        return None

    value = result.group(1)
    value = value.strip()
    value = value.split(" ")
    value = [x.replace("'", "") for x in value]
    value = [x.replace("\"", "") for x in value]
    value = [x.strip() for x in value]

    identifier = value[0]
    remaining = value[1:]

    group = SystemString.DEFAULT_GROUP

    while remaining:
        option = remaining.pop(0)
        if option == 'group':
            group = remaining.pop(0)

    if not re.search('^\w*$', identifier) or not \
            re.search('^\w*$', group):
        return None

    return (identifier, group)


def find_strings(path):
    strings = []

    for file_ in get_files(path):
        content = open(file_).read()
        strings += [parse_tmpl(x) for x in re.finditer(TMPL_PTRNS, content)]

        for ptn in API_PTRNS:
            strings += [parse_api(x) for x in re.finditer(ptn, content)]

    strings = filter(None, strings)
    return strings


class Command(BaseCommand):
    """
    Find and add system text to the various websites
    """
    def add_arguments(self, parser):
        parser.add_argument('--path', required=False)
        parser.add_argument('--dryrun', required=False)
        parser.add_argument('--limit', type=int, default=-1)
        parser.add_argument('--force', type=bool, default=False)

    def handle(self, *args, **options):
        path = options['path']
        dryrun = options['dryrun']
        limit = options['limit']
        force = options['force']

        if not path:
            path = os.getcwd()

        self.stdout.write('Using path "{}"'.format(path))

        strings = find_strings(path)
        sites = Site.objects.all()

        if limit != -1:
            strings = strings[:limit]

        self.stdout.write('Found {} strings'.format(len(strings)))

        if not force:
            proceed = raw_input('Proceed adding strings? (y/n): ')
            if proceed != 'y':
                return

        for string in strings:
            identifier, group = string
            self.stdout.write(u'Adding: {}:{}'.format(identifier, group))

            if dryrun:
                continue

            for site in sites:
                SystemString.objects.get_or_create(
                    identifier=identifier,
                    group=group,
                    site=site,
                )

        self.stdout.write('Done!')
