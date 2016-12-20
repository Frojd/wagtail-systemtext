from django.test import TestCase

from wagtailsystemtext.utils import (
    systemtext, set_site, fill_cache, preload, _cleanup,
)
from tests.factories import SiteFactory, PageFactory, SystemStringFactory


class ReplaceTestCase(TestCase):
    def tearDown(self):
        _cleanup()

    def test_replace(self):
        site = SiteFactory.create(
            root_page=PageFactory.create(title='mypage', path='00010002')
        )

        SystemStringFactory.create(
            identifier='headline',
            string='Headline!',
            site=site,
            modified=True,
        )

        set_site(site)
        fill_cache(site)
        preload(site)

        self.assertEquals(systemtext('headline'), 'Headline!')

    def test_group_replace(self):
        site = SiteFactory.create(
            root_page=PageFactory.create(title='mypage', path='00010002')
        )

        SystemStringFactory.create(
            identifier='sub_headline',
            string='My subheadline',
            group='sub',
            site=site,
            modified=True,
        )

        set_site(site)
        fill_cache(site)
        preload(site)

        self.assertEquals(systemtext('sub_headline', 'sub'), 'My subheadline')

    def test_two_sites(self):
        site = SiteFactory.create(
            root_page=PageFactory.create(title='mypage', path='00010002')
        )

        site_b = SiteFactory.create(
            root_page=PageFactory.create(title='mypage', path='00010003')
        )

        SystemStringFactory.create(
            identifier='headline',
            string='headline a',
            site=site,
            modified=True,
        )

        SystemStringFactory.create(
            identifier='headline',
            string='headline b',
            site=site_b,
            modified=True,
        )

        fill_cache(site)
        fill_cache(site_b)

        preload(site)
        preload(site_b)

        set_site(site)
        self.assertEquals(systemtext('headline'), 'headline a')

        set_site(site_b)
        self.assertEquals(systemtext('headline'), 'headline b')

    def test_empty_use_default(self):
        site = SiteFactory.create(
            root_page=PageFactory.create(title='mypage', path='00010002')
        )

        SystemStringFactory.create(
            identifier='title',
            string='',
            site=site,
            modified=False,
        )

        set_site(site)
        fill_cache(site)
        preload(site)

        self.assertEquals(systemtext('title', default='Default title'), 'Default title')

    def test_empty_but_modified(self):
        site = SiteFactory.create(
            root_page=PageFactory.create(title='mypage', path='00010002')
        )

        SystemStringFactory.create(
            identifier='title',
            string='',
            site=site,
            modified=True,
        )

        set_site(site)
        fill_cache(site)
        preload(site)

        self.assertEquals(systemtext('title', default='Default title'), '')
