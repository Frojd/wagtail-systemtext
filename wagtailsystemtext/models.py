from __future__ import unicode_literals

from django.db import models
from wagtail.wagtailcore.models import Site


class SystemString(models.Model):
    DEFAULT_GROUP = 'general'

    identifier = models.CharField(max_length=1024)
    string = models.CharField(max_length=1024, blank=True, null=True)
    group = models.CharField(max_length=255, default=DEFAULT_GROUP)

    site = models.ForeignKey(Site)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    accessed = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ['string', 'site', 'group']
