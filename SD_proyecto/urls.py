from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static 
from django.conf import settings

from SD_proyecto.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('income/', include('income.urls'))
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)