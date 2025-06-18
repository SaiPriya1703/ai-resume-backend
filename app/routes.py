from flask import Blueprint, request, jsonify
from app.chat import get_match_score

chat_routes = Blueprint('chat', __name__)

@chat_routes.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    resume = data.get("resume", "")
    job_description = data.get("job_description", "")
    
    if not resume or not job_description:
        return jsonify({"error": "Both resume and job description are required"}), 400

    response = get_match_score(resume, job_description)
    return jsonify(response)
