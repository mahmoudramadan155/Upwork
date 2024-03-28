# pip install faster-whisper
# pip install moviepy

import moviepy.editor as mp
from faster_whisper import WhisperModel
import os
from datetime import timedelta
import io

# convert mp4 to mp3
video_name = input("enter video name:")#'1-Getting Started with GPT-3 vs Open Source LLMs - LangChain 1'
full_path = os.path.join(os.getcwd(),video_name)
# Input video file path
video_path = f"{full_path}.mp4"
# Output audio file path
audio_path = f"{full_path}.mp3"

def video_to_audio(video_path, audio_path):
    # Convert video to audio
    video_clip = mp.VideoFileClip(video_path)
    # Create an in-memory file-like object
    audio_buffer = io.BytesIO()
    # Write audio to the in-memory buffer
    video_clip.audio.write_audiofile(audio_path, codec='mp3')
    # Set the buffer position to the beginning
    audio_buffer.seek(0)
    return audio_buffer

# Convert video to audio
# audio_buffer = video_to_audio(video_path, audio_path)

# convert mp3 to text 
model = WhisperModel("tiny")#tiny,base,small,medium,large-v2
segments, info = model.transcribe(audio_path)

for segment in segments:
    segmentId,startTime,endTime,text = segment.id,str(0)+str(timedelta(seconds=int(segment.start)))+',000', str(0)+str(timedelta(seconds=int(segment.end)))+',000', segment.text
    segment = f"{text[1:] if text[0] == ' ' else text}\n"

    srtFilename = f'{full_path}.srt'
    with open(srtFilename, 'a', encoding='utf-8') as srtFile:
        srtFile.write(segment)

