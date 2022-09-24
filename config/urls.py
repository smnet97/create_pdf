from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls'))
]

urlpatterns += static(settings.STATIC_URL, documnet_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, documnet_root=settings.MEDIA_ROOT)
