from django.shortcuts import render
from utils.music_downloader import download_music
from utils.whisper_setup import transcribe, format_transcription_to_str
from .forms import URLForm
from edits_ai.settings import MEDIA_URL


def home(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            file_name = MEDIA_URL + download_music(url)
            lyrics = transcribe(file_name)
            lyrics_formatted = format_transcription_to_str(lyrics)
            return render(request, 'home.html', {'form': form, 'file_name': file_name, 'lyrics_formatted': lyrics_formatted})
    else:
        form = URLForm()

    return render(request, 'home.html', {'form': form})
