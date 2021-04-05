from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from bookmark.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    url(r'^bookmark/', BookmarkLV.as_view(), name='index'),
    url(r'^bookmark/(?P<pk>\d+)/$'), BookmarkDV.as_view(), name='detail'),
]
