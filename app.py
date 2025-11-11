from flask import Flask, request, jsonify, render_template
from datetime import datetime
from stage_disease_model import calculate_days_since_sowing, predict_stage, get_possible_diseases, explain_disease
from gemini_integration import configure_gemini, query_gemini
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# Configure Gemini with API key from environment variables
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in .env file")
configure_gemini(api_key)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict_stage_disease", methods=["POST"])
def predict_stage_disease():
    data = request.json
    crop_name = data.get("crop_name", "Toor")
    sowing_date_str = data.get("sowing_date")
    current_date_str = data.get("current_date")

    # parse dates
    try:
        sowing_date = datetime.strptime(sowing_date_str, "%d-%m-%Y")
        current_date = datetime.strptime(current_date_str, "%Y-%m-%d")
    except Exception as e:
        return jsonify({"error": "Invalid date format. Use DD-MM-YYYY for sowing_date and YYYY-MM-DD for current_date."}), 400

    days_since = calculate_days_since_sowing(sowing_date, current_date)
    stage = predict_stage(days_since)
    diseases = get_possible_diseases(stage)
    disease_details = {d: explain_disease(d) for d in diseases}

    return jsonify({
        "crop_name": crop_name,
        "days_since_sowing": days_since,
        "predicted_stage": stage,
        "possible_diseases": disease_details
    })

@app.route("/get_insights", methods=["POST"])
def get_insights():
    data = request.json
    crop_name = data.get("crop_name", "Toor")
    stage = data.get("stage")
    disease = data.get("disease")

    if not disease:
        return jsonify({"error": "Please provide disease for insights."}), 400

    prompt = (
        f"Crop: {crop_name}\n"
        f"Current stage: {stage}\n"
        f"Disease: {disease}\n"
        "Explain the affecting factors, symptoms, and suggest chemical and organic treatment options."
    )

    insights = query_gemini(prompt)
    return jsonify({"insights": insights})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
