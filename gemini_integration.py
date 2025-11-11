import google.generativeai as genai
import os

# A simple in-memory cache
gemini_cache = {}

def configure_gemini(api_key):
    genai.configure(api_key=api_key)

def query_gemini(prompt):
    if prompt in gemini_cache:
        return gemini_cache[prompt]

    model = genai.GenerativeModel('models/gemini-pro-latest')
    try:
        response = model.generate_content(prompt)
        result = "".join(part.text for part in response.parts)
        gemini_cache[prompt] = result  # Cache the result
        return result
    except Exception as e:
        return f"Error: {e}"
