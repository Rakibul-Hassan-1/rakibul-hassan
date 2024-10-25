from django.shortcuts import render
from django.http import HttpResponse
from .models import UploadedFile
from .forms import UploadFileForm
from googletrans import Translator
import pysrt
import tempfile
import os

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

from django.http import HttpResponse

def task2(request):
    form = UploadFileForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        new_file = UploadedFile(file=request.FILES['file'])
        new_file.save()
        processed_text = process_srt_file(new_file.file.path)
        response = HttpResponse(processed_text, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename="processed.txt"'
        return response
    return render(request, 'upload.html', {'form': form})

def task1(request):
    form = UploadFileForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        with tempfile.NamedTemporaryFile(delete=False, suffix='.srt') as temp:
            temp.write(request.FILES['file'].read())
            temp.close()
            try:
                subs = pysrt.open(temp.name, encoding='utf-8')
                translator = Translator()
                for sub in subs:
                    sub.text = translator.translate(sub.text, src='zh-cn', dest='en').text
                with tempfile.NamedTemporaryFile(delete=False, suffix='.srt') as translated_temp:
                    subs.save(translated_temp.name, encoding='utf-8')
                    with open(translated_temp.name, 'rb') as file:
                        response = HttpResponse(file.read(), content_type='application/x-subrip')
                        response['Content-Disposition'] = 'attachment; filename="translated_subtitles.srt"'
            finally:
                os.unlink(temp.name)
                os.unlink(translated_temp.name)
            return response
        return HttpResponse("Error processing the subtitles.", status=400)
    return render(request, 'file.html', {'form': form})


def file_upload(request):
    form = UploadFileForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        new_file = UploadedFile(file=request.FILES['file'])
        new_file.save()
        processed_text = process_srt_file(new_file.file.path)
        response = HttpResponse(processed_text, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename="processed.txt"'
        return response
    return render(request, 'upload.html', {'form': form})

def upload_file(request):
    form = UploadFileForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        with tempfile.NamedTemporaryFile(delete=False, suffix='.srt') as temp:
            temp.write(request.FILES['file'].read())
            temp.close()
            try:
                subs = pysrt.open(temp.name, encoding='utf-8')
                translator = Translator()
                for sub in subs:
                    sub.text = translator.translate(sub.text, src='zh-cn', dest='en').text
                with tempfile.NamedTemporaryFile(delete=False, suffix='.srt') as translated_temp:
                    subs.save(translated_temp.name, encoding='utf-8')
                    with open(translated_temp.name, 'rb') as file:
                        response = HttpResponse(file.read(), content_type='application/x-subrip')
                        response['Content-Disposition'] = 'attachment; filename="translated_subtitles.srt"'
            finally:
                os.unlink(temp.name)
                os.unlink(translated_temp.name)
            return response
        return HttpResponse("Error processing the subtitles.", status=400)
    return render(request, 'file.html', {'form': form})

def process_srt_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = [line.strip() for line in file if line.strip() and not line.strip().isdigit() and '-->' not in line]
    return ' '.join(text)
