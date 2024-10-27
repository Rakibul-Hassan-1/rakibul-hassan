from django.urls import include, path
from subtitles.views import file_upload
from subtitles.views import upload_file

urlpatterns = [
    path('', include('subtitles.urls')), 
    path('speech_app/', include('speech_app.urls')),
]
