from django.contrib import admin
from django.urls import path

from bookmark.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('bookmark/', BookmarkLV.as_view(), name='index'),
    path('bookmark/(?P<pk>\d+)/$'), BookmarkDV.as_view(), name='detail'),
]
