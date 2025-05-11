
import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

SERP_API_KEY = os.getenv("SERP_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def perform_search(query, num_results=3):
    url = f"https://serpapi.com/search.json?q={query}&num={num_results}&api_key={SERP_API_KEY}"
    response = requests.get(url)
    data = response.json()
    urls = [item['link'] for item in data.get('organic_results', [])[:num_results]]
    return urls

def extract_and_clean(urls):
    content = ""
    for url in urls:
        try:
            page = requests.get(url, timeout=10)
            soup = BeautifulSoup(page.content, 'html.parser')
            for tag in soup(['script', 'style', 'header', 'footer', 'nav', 'aside']):
                tag.decompose()
            text = ' '.join(p.get_text() for p in soup.find_all(['h1', 'h2', 'p']))
            content += text + "\n"
        except Exception as e:
            print(f"Failed to fetch {url}: {e}")
    return content.strip()

def generate_llm_response(query, context):
    prompt = f"Answer the following question based on the provided context.\n\nContext:\n{context}\n\nQuestion: {query}\n\nAnswer:"

    try:
        response = requests.post(
            "https://api.openai.com/v1/completions",
            headers={
                "Authorization": f"Bearer {OPENAI_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "text-davinci-003",
                "prompt": prompt,
                "temperature": 0.7,
                "max_tokens": 300
            }
        )
        json_data = response.json()
        print("OpenAI Response JSON:", json_data)
        if "choices" in json_data:
          return json_data["choices"][0]["text"].strip()
        elif "error" in json_data:
          return f"OpenAI error: {json_data['error']['message']}"
        else:
          return "Unexpected response format from OpenAI."
