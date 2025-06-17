import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_resume(resume_text, job_description):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that analyzes resumes."},
            {"role": "user", "content": f"Resume:\n{resume_text}"},
            {"role": "user", "content": f"Job Description:\n{job_description}"},
            {"role": "user", "content": "Compare the resume and job description. Suggest missing skills and improvements."}
        ]
    )
    return response.choices[0].message.content
