from flask import Blueprint, request, jsonify
import os
from llama_cpp import Llama

# Setup Blueprint
chat_routes = Blueprint("chat", __name__)

# Load Mistral model on startup
model_path = os.getenv("MODEL_PATH", "app/models/mistral")
llm = Llama(model_path=f"{model_path}/mistral-7b-instruct-v0.1.Q4_K_M.gguf", n_ctx=2048)

# Resume Matching
def extract_skills(text):
    # Very basic skill extraction — can improve later
    keywords = ["Python", "Flask", "SQL", "MongoDB", "Machine Learning", "React", "HTML", "CSS", "JavaScript"]
    return [skill for skill in keywords if skill.lower() in text.lower()]

def get_match_score(resume, job_description):
    resume_skills = extract_skills(resume)
    job_skills = extract_skills(job_description)
    
    matched = set(resume_skills) & set(job_skills)
    missing = set(job_skills) - set(resume_skills)

    percentage = round(len(matched) / len(job_skills) * 100, 2) if job_skills else 0

    return {
        "matched_skills": list(matched),
        "missing_skills": list(missing),
        "match_percentage": percentage
    }

# API to get match score
@chat_routes.route("/match", methods=["POST"])
def match_resume():
    data = request.get_json()
    resume = data.get("resume", "")
    job_desc = data.get("job_description", "")

    result = get_match_score(resume, job_desc)
    return jsonify(result)

# API to get AI response using Mistral
@chat_routes.route("/chat", methods=["POST"])
def chat_with_model():
    data = request.get_json()
    prompt = data.get("message", "")
    
    full_prompt = f"Q: {prompt}\nA:"
    reply = llm(full_prompt, max_tokens=100)
    answer = reply["choices"][0]["text"].strip()
    
    return jsonify({"response": answer})
