from django.conf import global_settings
from django.template import Context, Template
from django.test import TestCase, modify_settings, override_settings

from wagtailsystemtext.utils import (
    set_site, fill_cache, preload, _cleanup,
)
from tests.factories import SiteFactory, PageFactory, SystemStringFactory


@override_settings(
    MIDDLEWARE=global_settings.MIDDLEWARE,
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
    def tearDown(self):
        _cleanup()

    def setUp(self):
        site = SiteFactory.create(
            root_page=PageFactory.create(title='mypage', path='00010002')
        )

        SystemStringFactory.create(
            identifier='title',
            string='Headline!',
            site=site,
            modified=True,
        )

        SystemStringFactory.create(
            identifier='subtitle',
            string='Sub Headline!',
            group='sub',
            site=site,
            modified=True,
        )

        SystemStringFactory.create(
            identifier='new_link',
            string='',
            site=site,
            modified=False,
        )

        SystemStringFactory.create(
            identifier='empty_link',
            string='',
            site=site,
            modified=True,
        )

        set_site(site)
        fill_cache(site)
        preload(site)

    def test_systemtext_tag(self):
        out = Template(
            "{% load systemtext %}"
            "{% systemtext \"title\" %}"
        ).render(Context({
        }))

        self.assertTrue('Headline!' in out)

    def test_systemtext_tag(self):
        out = Template(
            "{% load systemtext %}"
            "{% systemtext \"subtitle\" group \"sub\" %}"
        ).render(Context({
        }))

        self.assertTrue('Sub Headline!' in out)

    def test_systemtext_variable_tag(self):
        out = Template(
            "{% load systemtext %}"
            "{% systemtext title_var group \"sub\" %}"
        ).render(Context({
            'title_var': 'subtitle',
        }))

        self.assertTrue('Sub Headline!' in out)

    def test_systemtext_variable_as_var(self):
        out = Template(
            "{% load systemtext %}"
            "{% systemtext title_var group \"sub\" as my_var %}"
            "hello_{{my_var}}"
        ).render(Context({
            'title_var': 'subtitle',
        }))

        self.assertTrue('hello_Sub Headline!' in out)

    def test_systemtext_tag_default(self):
        out = Template(
            "{% load systemtext %}"
            "{% systemtext \"new_link\" default \"Wow!\"%}"
        ).render(Context({
        }))

        self.assertTrue('Wow!' in out)

    def test_systemtext_tag_empty_no_default(self):
        out = Template(
            "{% load systemtext %}"
            "{% systemtext \"empty_link\" default \"Wow!\"%}"
        ).render(Context({
        }))

        self.assertTrue('' in out)
