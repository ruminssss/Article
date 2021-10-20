from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.views import serve
from django.views.static import serve as media_serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
if not settings.DEBUG:
    urlpatterns.append(path('static/<path:path>', serve, {'insecure':True}))
    urlpatterns.append(path('media/<path:path>', media_serve, {'document_root':settings.MEDIA_ROOT}))
