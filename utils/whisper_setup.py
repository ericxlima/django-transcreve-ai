import whisper
from pprint import pprint
from typing import List, Dict
from django.utils.html import linebreaks

model = whisper.load_model('base')
options = whisper.DecodingOptions(without_timestamps=True)


def transcribe(audio_path) -> List[Dict]:
    result = model.transcribe(audio_path, word_timestamps=True)
    output = []
    for segment in result['segments']:
        output.append({
            "text": segment['text'],
            "start": segment['start'],
            "end": segment['end'],
        })
    return output


def format_transcription_to_str(transcription: List[Dict]) -> List[str]:
    formatted_strings = []
    number_of_caracters = len(str(transcription[-1]['end']))
    for segment in transcription:
        start = "{:.2f}".format(
            float(segment['start'])).zfill(number_of_caracters)
        end = "{:.2f}".format(float(segment['end'])).zfill(number_of_caracters)
        formatted_strings.append(f"{start} : {end} ->{segment['text']}")
    return formatted_strings
