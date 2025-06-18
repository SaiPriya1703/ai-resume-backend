from flask import Blueprint, request, jsonify
from llama_cpp import Llama
import os

# Define Blueprint
chat_routes = Blueprint("chat_routes", __name__)

# ✅ Dynamically get the model path from environment variable
# Defaults to "app/models/mistral" for local testing
base_path = os.getenv("MODEL_PATH", "app/models/mistral")
model_file = "mistral-7b-instruct-v0.1.Q4_K_M.gguf"
MODEL_PATH = os.path.join(base_path, model_file)

# ✅ Load model
llm = Llama(model_path=MODEL_PATH, n_ctx=2048)

@chat_routes.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_prompt = data.get("message", "")
        
        full_prompt = f"Q: {user_prompt}\nA:"
        response = llm(full_prompt, max_tokens=100)
        answer = response["choices"][0]["text"].strip()

        return jsonify({"response": answer})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
