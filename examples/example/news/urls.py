from __future__ import absolute_import

from django.urls import re_path as url

from .views import browse, detail

__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = (
    'urlpatterns',
)

app_name="news"

urlpatterns = [
    # Listing URL
    url(r'^$', view=browse, name='browse'),

    # Detail URL
    url(r'^(?P<slug>(?!overview\-)[\w\-\_\.\,]+)/$',
        view=detail,
        name='detail'),
]

