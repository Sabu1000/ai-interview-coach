import os

from extract_frames import extract_frames
from audio_extractor import extract_audio
from emotion_analyzer import analyze_emotions_in_frames
from feedback_generator import generate_interview_feedback
from nlp_analysis import analyze_transcript
from transcript_generator import transcribe_audio


def main():
    # get video input
    video_path = "videos/sample_interview.mp4"
    frames_dir = "frames"
    audio_path = "output_audio.wav"

    print(f"Processing video: {video_path}")

    # Step 2 - Get Frames
    print("\nExtracting video frames...")
    extract_frames(video_path, frames_dir, interval_seconds=1)

    # Step 3 - Get audio
    print("\nExtracting audio from video...")
    extract_audio(video_path, output_audio_path=audio_path)

    # Step 4 - Transcribe audio
    print("\nTranscribing audio...")
    transcript = transcribe_audio(audio_path)
    with open("transcript.txt", "w", encoding="utf-8") as f:
        f.write(transcript)

    # Step 5 - Get emotion
    print("\nAnalyzing facial emotion...")
    emotion_result = analyze_emotions_in_frames(frames_dir)

    # Step 6 - NLP analysis
    print("\nAnalyzing language...")
    nlp_analysis = analyze_transcript(transcript)

    # Step 7 - Generate feedback
    print("\nGenerating feedback...")
    feedback = generate_interview_feedback(transcript, emotion_result, nlp_analysis)

    print("\nFinal feedback: \n")
    print(feedback)


if __name__ == "__main__":
    main()
