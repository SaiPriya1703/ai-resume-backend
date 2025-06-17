from flask import Flask, request, jsonify
from llama_cpp import Llama

app = Flask(__name__)

# Load Mistral model once when the server starts
MODEL_PATH = "C:/Users/pshivasantoshreddy/Documents/models/mistral/mistral-7b-instruct-v0.1.Q4_K_M.gguf"
llm = Llama(model_path=MODEL_PATH, n_ctx=2048)

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_prompt = data.get("message", "")
        
        # Format the prompt like instruct models expect
        full_prompt = f"Q: {user_prompt}\nA:"

        response = llm(full_prompt, max_tokens=100)

        answer = response["choices"][0]["text"].strip()
        return jsonify({"response": answer})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
