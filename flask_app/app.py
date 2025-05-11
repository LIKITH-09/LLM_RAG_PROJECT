import os
print("Loaded OpenAI Key:", os.getenv("OPENAI_API_KEY"))
from flask import Flask, request, jsonify
from utils import perform_search, extract_and_clean, generate_llm_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/query", methods=["POST"])
def handle_query():
    data = request.get_json()
    query = data.get("query")
    urls = perform_search(query)
    context = extract_and_clean(urls)
    response = generate_llm_response(query, context)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
