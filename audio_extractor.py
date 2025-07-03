from moviepy import VideoFileClip
import os

def extract_audio(video_path, output_audio_path="output_audio.wav"):
    video = VideoFileClip(video_path) # load video into memory and make it acessable
    video.audio.write_audiofile(output_audio_path, codec='pcm_s16le') # access just the audio portion and save the file to the specified path
    video.close() # close video
    print(f'[INFO] Audio extracted and saved to: {output_audio_path}')
    return output_audio_path