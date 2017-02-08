from django.conf.urls import url, include
from django.http import HttpResponse

from wagtailsystemtext.utils import systemtext_lazy as _st


def headline_view(request):
    return HttpResponse(_st('title'))


urlpatterns = [
    url('^test-title$', headline_view, name='headline_view'),
]
