from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
]

# Serve user-uploaded media files during development.
# (Static files under STATICFILES_DIRS are served automatically by
# django.contrib.staticfiles when DEBUG=True, no extra config needed.)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
