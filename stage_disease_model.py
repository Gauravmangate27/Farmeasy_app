# stage_disease_model.py

from disease_data import stage_durations, stage_diseases, disease_info

def calculate_days_since_sowing(sowing_date, current_date):
    return (current_date - sowing_date).days

def predict_stage(days_since_sowing):
    for stage, (start, end) in stage_durations.items():
        if start <= days_since_sowing <= end:
            return stage
    if days_since_sowing > 180:
        return "Maturity"
    return "Unknown"

def get_possible_diseases(stage):
    return stage_diseases.get(stage, [])

def explain_disease(disease):
    return disease_info.get(disease, "No details available.")
