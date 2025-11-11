from stage_disease_model import calculate_days_since_sowing, predict_stage, get_possible_diseases, explain_disease
from gemini_integration import GeminiLLM
from datetime import datetime

def main():
    print("=== Toor Crop Stage and Disease Prediction ===")
    crop_name = input("Enter crop name (e.g., Toor): ").strip()
    sowing_date_str = input("Enter sowing date (DD-MM-YYYY): ").strip()
    current_date_str = input("Enter current date (YYYY-MM-DD): ").strip()
    sowing_date = datetime.strptime(sowing_date_str, "%d-%m-%Y")
    current_date = datetime.strptime(current_date_str, "%Y-%m-%d")

    days_since = calculate_days_since_sowing(sowing_date, current_date)
    stage = predict_stage(days_since)
    
    print(f"\nCurrent crop stage based on dates: {stage}")
    possible_diseases = get_possible_diseases(stage)
    
    if not possible_diseases:
        print("No known diseases predicted at this stage.")
        return
    
    print("\nPossible diseases at this stage:")
    for i, disease in enumerate(possible_diseases, 1):
        print(f"{i}. {disease} - {explain_disease(disease)}")

    selected_idx = int(input("\nChoose the disease number for detailed insight: "))
    selected_disease = possible_diseases[selected_idx - 1]

    # Prepare prompt for Gemini LLM
    prompt = (
        f"Crop: {crop_name}\n"
        f"Current stage: {stage}\n"
        f"Disease: {selected_disease}\n"
        f"Explain the affecting factors, symptoms, and provide chemical and organic treatment suggestions for this disease."
    )

    # Initialize Gemini LLM (replace 'your_api_key' with actual key)
    api_key = "AIzaSyDfxry1eaZsMsWfwljT3Dl-7OWeEpHypoc"
    gemini = GeminiLLM(api_key)
    insights = gemini.query_llm(prompt)

    print("\n=== Gemini-2.5-Flash LLM Insights ===")
    print(insights)

if __name__ == "__main__":
    main()
