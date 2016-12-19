from django.conf import global_settings
from django.template import Context, Template
from django.test import TestCase, modify_settings, override_settings

from wagtailsystemtext.utils import gettext, set_site, fill_cache, preload
from tests.factories import SiteFactory, PageFactory, SystemStringFactory

@override_settings(
    MIDDLEWARE_CLASSES=global_settings.MIDDLEWARE_CLASSES,
    TEMPLATES=[{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': True,
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.core.context_processors.debug',
                'django.core.context_processors.i18n',
                'django.core.context_processors.media',
                'django.core.context_processors.static',
                'django.core.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.request',
            ],
        },
    }],
    SITE_ID=1
)
class TemplateFiltersTestCase(TestCase):
    def setUp(self):
        site = SiteFactory.create(
            root_page=PageFactory.create(title='mypage', path='00010002')
        )

        SystemStringFactory.create(
            identifier='title',
            string='Headline!',
            site=site,
        )

        SystemStringFactory.create(
            identifier='subtitle',
            string='Sub Headline!',
            group='sub',
            site=site,
        )

        set_site(site)
        fill_cache(site)
        preload(site)

    def test_trans_tag(self):
        out = Template(
            "{% load systemtext %}"
            "{% st_trans \"title\" %}"
        ).render(Context({
        }))

        self.assertTrue('Headline!' in out)

    def test_trans_tag(self):
        out = Template(
            "{% load systemtext %}"
            "{% st_trans \"subtitle\" group \"sub\" %}"
        ).render(Context({
        }))

        self.assertTrue('Sub Headline!' in out)

    def test_trans_variable_tag(self):
        out = Template(
            "{% load systemtext %}"
            "{% st_trans title_var group \"sub\" %}"
        ).render(Context({
            'title_var': 'subtitle',
        }))

        self.assertTrue('Sub Headline!' in out)
