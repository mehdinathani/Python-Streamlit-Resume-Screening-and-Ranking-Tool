# utils/ai_feedback.py
import requests
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env.local")

def generate_feedback(resume_text):
    """
    Uses Hugging Face's free inference API with an open-source model
    """
    API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3"
    headers = {"Authorization": f"Bearer {os.getenv('HF_API_KEY')}"}

    prompt = f"""Resume Feedback: Analyze this resume and provide 3 concise improvements:
    {resume_text}
    Feedback:"""

    try:
        response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
        response.raise_for_status()
        return response.json()[0]['generated_text']
    except Exception as e:
        return f"Basic feedback: Focus on quantifying achievements and using action verbs. Error: {str(e)}"