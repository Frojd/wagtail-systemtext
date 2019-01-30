from django.conf import global_settings
from django.test import TestCase, override_settings
from wagtail.core.models import Site

from wagtailsystemtext.utils import _cleanup
from tests.factories import SiteFactory, PageFactory, SystemStringFactory



@override_settings(
    MIDDLEWARE=global_settings.MIDDLEWARE + [
        'wagtail.core.middleware.SiteMiddleware',
        'wagtailsystemtext.middlewares.SiteSystemTextMiddleware',
    ],
    ALLOWED_HOSTS=['*'],
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
                'django.core.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    }],
    SITE_ID=1
)
class MiddlewareSitesTestCase(TestCase):
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

        self.site = site

    def test_no_sites_systemtext(self):
        Site.objects.all().delete()

        resp = self.client.get('/test-title')
        self.assertTrue(not resp.content)

    def test_with_site(self):
        resp = self.client.get('/test-title', SERVER_NAME=self.site.hostname)
        content = resp.content.decode('utf-8')
        self.assertTrue(content == u'Headline!')
