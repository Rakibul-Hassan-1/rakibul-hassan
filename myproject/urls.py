from django.urls import include, path
from subtitles.views import file_upload
from subtitles.views import upload_file
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('subtitles.urls')), 
    path('speech_app/', include('speech_app.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)