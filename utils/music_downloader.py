import os
from pytube import YouTube
import uuid
from edits_ai.settings import MEDIA_URL


def download_music(url: str, path: str = MEDIA_URL) -> str:
    """Download music from YouTube.

    Args:
        url (str): URL from YouTube.
        path (str): path to output folder.
    """
    if not os.path.exists(path):
        os.makedirs(path)

    yt = YouTube(url)
    file_name = str(uuid.uuid4())
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_stream.download(output_path=path, filename=file_name)
    return file_name
