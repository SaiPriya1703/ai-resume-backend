from llama_cpp import Llama

# Change path to match your actual downloaded GGUF model file
MODEL_PATH = "C:/Users/pshivasantoshreddy/Documents/models/mistral/mistral-7b-instruct-v0.1.Q4_K_M.gguf"

# Load model
llm = Llama(model_path=MODEL_PATH, n_ctx=2048)

# Ask a question
response = llm("Q: What is the capital of India?\nA:", max_tokens=100)

print(response["choices"][0]["text"])
