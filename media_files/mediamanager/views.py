from django.shortcuts import render
from .models import Media
# Create your views here.

def media_list(request):
    audio_files = Media.objects.audio()
    video_files = Media.objects.video()
    image_files = Media.objects.images()

    context = {
        'audio_files': audio_files,
        'video_files': video_files,
        'image_files': image_files,
    }

    return render(request, 'mediamanager/media_list.html', context)
