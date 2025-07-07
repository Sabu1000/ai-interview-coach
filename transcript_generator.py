import whisper

def transcribe_audio(audio_path):
    model = whisper.load_model("base")  

    result = model.transcribe(audio_path, language="en", fp16=False)

    transcript = result['text']
    print("[INFO] Transcription Complete:\n")
    print(transcript)

    return transcript
