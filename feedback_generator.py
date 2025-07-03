import os
from openai import OpenAI


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_interview_feedback(transcript, emotion_results, nlp_results):
    emotion_summary = "\n".join([f"{k}: {v}" for k, v in emotion_results.items()])

    filler_text = ", ".join([f"{word} ({count})" for word, count in nlp_results["filter_counts"].items()])

    polarity = nlp_results["sentiment"]["polarity"]
    subjectivity = nlp_results["sentiment"]["subjectivity"]

    prompt = f"""

    You're an AI interview coach. Based on the following input, generate feedback for the user:

    1. TRANSCRIPT:
    \"\"\"{transcript}\"\"\"

    2. EMOTION TIMELINE (per video frame):
    {emotion_summary}

    3. FILLER WORDS:
    {filler_text if filler_text else "No major filler words detected."}

    4. SENTIMENT:
    - Polarity: {polarity:.2f}
    - Subjectivity: {subjectivity:.2f}

    Please provide:
    - Constructive feedback on the user's communication style
    - Observations on confidence based on emotions
    - Areas for improvement
    - Encouragement and praise where appropriate

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


 
