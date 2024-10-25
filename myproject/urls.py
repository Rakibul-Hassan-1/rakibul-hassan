from django.urls import path
from subtitles.views import file_upload
from subtitles.views import upload_file

urlpatterns = [

    path('', file_upload, name='file_upload'),
    path('srt/', upload_file, name='upload_file'),

]
