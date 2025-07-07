import os
from openai import OpenAI


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_interview_feedback(transcript, emotion_results, nlp_results, job_title="Software Engineer"):
    emotion_summary = "\n".join([f"{k}: {v}" for k, v in emotion_results.items()])

    filler_text = ", ".join([f"{word} ({count})" for word, count in nlp_results["filter_counts"].items()])

    polarity = nlp_results["sentiment"]["polarity"]
    subjectivity = nlp_results["sentiment"]["subjectivity"]

    prompt = f"""

    You are an expert career coach and interviewer.

    The candidate is applying for a **{job_title}** role. Below is their interview and performance data.

    1. TRANSCRIPT:
    \"\"\"{transcript}\"\"\"

    2. EMOTION TIMELINE (per video frame):
    {emotion_summary}

    3. FILLER WORDS:
    {filler_text if filler_text else "No major filler words detected."}

    4. SENTIMENT:
    - Polarity: {polarity:.2f}
    - Subjectivity: {subjectivity:.2f}

    Please:
    1. Evaluate the answer as if you're interviewing them for a {job_title}.
    2. Compare their response to what you'd expect from a top {job_title} candidate.
    3. Highlight strengths and areas of improvement in communication and content.
    4. Give personalized, encouraging feedback.

    """
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a professional career coach specializing in mock interview feedback."},
                {"role": "user", "content": prompt}
            ],
            temperature = 0.7,
        )
        feedback = response.choices[0].message.content
        return feedback
    except Exception as e:
        return f"Error generating feedback {str(e)}"


 
