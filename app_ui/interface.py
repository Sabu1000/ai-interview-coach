import streamlit as st
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from extract_frames import extract_frames
from audio_extractor import extract_audio
from transcript_generator import transcribe_audio
from emotion_analyzer import analyze_emotions_in_frames
from nlp_analysis import analyze_transcript
from feedback_generator import generate_interview_feedback


st.set_page_config(page_title = "AI Interview Coach", layout = "wide")
st.title("AI Interview Coach")
st.write("Upload your mock interview video below: ")

# upload video file
uploaded_video = st.file_uploader("Choose a .mp4 file", type=["mp4"])

if uploaded_video is not None:
    video_path = os.path.join("videos", uploaded_video.name)
    with open(video_path, "wb") as f:
        f.write(uploaded_video.read())

    st.success("Video uploaded sucessfully!")

    # analysis pipeline
    with st.spinner("Extracting frames..."):
        extract_frames(video_path, "frames", interval_seconds=1)
    
    with st.spinner("Extracting and transcribing audio..."):
        audio_path = "output_audio.wav"
        extract_audio(video_path, output_audio_path=audio_path)
        transcript = transcribe_audio(audio_path)

    st.subheader("Transcript")
    st.text_area("Full Transcript", transcript, height=200)

    with st.spinner("Analyzing emotions..."):
        emotions = analyze_emotions_in_frames("frames")

    st.subheader("Detected Emotions")
    st.json(emotions)

    with st.spinner("Running NLP analysis..."):
        nlp_results = analyze_transcript(transcript)

    st.subheader("NLP Results")
    st.json(nlp_results)

    job_title = st.text_input("Enter the target job title (e.g., Product Manager): ", value="Software Engineer")

    with st.spinner("Generating AI feedback..."):
        feedback = generate_interview_feedback(transcript, emotions, nlp_results)

    st.subheader("AI Feedback Summary")
    st.write(feedback)