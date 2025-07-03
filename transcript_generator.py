import whisper

def transcribe_audio(audio_path):
    model = whisper.load_model("base")  

    # Force language to English and disable fp16 for better CPU accuracy
    result = model.transcribe(audio_path, language="en", fp16=False)

    transcript = result['text']
    print("[INFO] Transcription Complete:\n")
    print(transcript)

    return transcript
