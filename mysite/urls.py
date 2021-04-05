from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^bookmark/', include('bookmark.urls')),
    url(r'^blog/', include('blog.urls')),
]
