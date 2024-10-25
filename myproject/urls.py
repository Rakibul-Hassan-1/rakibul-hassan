from django.urls import include, path
from subtitles.views import file_upload
from subtitles.views import upload_file

urlpatterns = [
    path('', include('subtitles.urls')), 
]
