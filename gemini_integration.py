import google.generativeai as genai
import os

def configure_gemini(api_key):
    genai.configure(api_key=api_key)

def query_gemini(prompt):
    model = genai.GenerativeModel('models/gemini-pro-latest')
    try:
        response = model.generate_content(prompt)
        return "".join(part.text for part in response.parts)
    except Exception as e:
        return f"Error: {e}"
