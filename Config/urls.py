from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from django.contrib import admin


urlpatterns = [
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
