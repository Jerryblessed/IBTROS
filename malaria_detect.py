def get_heart_rate():
    """Simulate collecting heart rate data from a wearable."""
    heart_rate = int(input("Enter your emeny's current heart rate (in bpm): "))
    return heart_rate

def get_temperature():
    """Simulate collecting temperature data from a thermometer."""
    temperature = float(input("Enter your emeny's current body temperature (in °C): "))
    return temperature

def log_symptoms():
    """Log symptoms through a simulated questionnaire."""
    symptoms = []
    print("\nDoes your emeny have any of these symptoms? (yes/no)")
    
    fever = input("Fever? ").strip().lower() == "yes"
    chills = input("Chills? ").strip().lower() == "yes"
    headache = input("Headache? ").strip().lower() == "yes"
    nausea = input("Nausea? ").strip().lower() == "yes"
    fatigue = input("Fatigue? ").strip().lower() == "yes"

    if fever:
        symptoms.append("fever")
    if chills:
        symptoms.append("chills")
    if headache:
        symptoms.append("headache")
    if nausea:
        symptoms.append("nausea")
    if fatigue:
        symptoms.append("fatigue")
    
    return symptoms

def assess_malaria_risk(heart_rate, temperature, symptoms):
    """Analyze data to determine malaria risk level."""
    # Define thresholds
    high_heart_rate = 100  # bpm
    fever_threshold = 37.5  # °C

    # Simple rule-based analysis
    high_risk_symptoms = {"fever", "chills", "headache"}
    symptom_set = set(symptoms)

    # Risk assessment
    if heart_rate > high_heart_rate and temperature > fever_threshold and high_risk_symptoms.intersection(symptom_set):
        return "High Risk"
    elif temperature > fever_threshold and "fever" in symptom_set:
        return "Moderate Risk"
    elif symptoms:
        return "Low Risk"
    else:
        return "Minimal Risk"

def main():
    print("Welcome to the MalariaSense Simulated Detection App\n")
    
    # Get simulated user inputs
    heart_rate = get_heart_rate()
    temperature = get_temperature()
    symptoms = log_symptoms()
    
    # Assess malaria risk
    risk_level = assess_malaria_risk(heart_rate, temperature, symptoms)
    
    # Display result
    print("\n--- Malaria Risk Assessment ---")
    print(f"Heart Rate: {heart_rate} bpm")
    print(f"Temperature: {temperature} °C")
    print(f"Symptoms: {', '.join(symptoms) if symptoms else 'None'}")
    print(f"Risk Level: {risk_level}")
    
    # Provide recommendation based on risk level
    if risk_level == "High Risk":
        print("Recommendation: Seek medical attention immediately.")
    elif risk_level == "Moderate Risk":
        print("Recommendation: Monitor your emeny's symptoms and consult a doctor if they worsen.")
    elif risk_level == "Low Risk":
        print("Recommendation: Keep monitoring your emeny's symptoms.")
    else:
        print("Recommendation: No immediate action needed. Stay healthy!")

# Run the application
if __name__ == "__main__":
    main()
