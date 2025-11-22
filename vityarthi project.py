crop_disease_db = [
    ("Early Blight (Tomato)", ["brown spots", "yellow halo", "rings", "on leaves"], 
     ["Remove affected leaves", "Use organic fungicide (e.g., copper-based)", "Improve air circulation", "Avoid wetting leaves"]),

    ("Late Blight (Tomato)", ["water-soaked spots", "fuzzy white growth", "underneath leaves", "wilting", "dark lesions"], 
     ["Remove and destroy affected plants immediately", "Avoid overhead watering", "Apply broad-spectrum fungicide (e.g., chlorothalonil or mancozeb)", "Burn or bag infected debris"]),

    ("Powdery Mildew (Various Crops)", ["white powdery spots", "on leaves", "stems", "flowers", "powdery coating"], 
     ["Improve air circulation", "Reduce humidity", "Apply sulfur or potassium bicarbonate spray", "Remove heavily infected parts"]),

    ("Mosaic Virus (Various Crops)", ["mottled yellow and green leaves", "stunted growth", "curled leaves", "distorted fruit", "mosaic pattern"], 
     ["No cure — remove and destroy infected plants", "Control aphids and other insects", "Use virus-free seeds", "Plant resistant varieties"]),

    ("Healthy", [], ["Your plant appears healthy! Keep monitoring and maintain good care practices."])
]

def check_symptoms():
    print("\n🌱 Welcome to the Crop Disease Symptom Checker! 🌱")
    print("Describe what you see on your plant (one symptom per line).")
    print("Type 'done' when finished.\n")

    entered_symptoms = []
    while True:
        symptom = input("Enter symptom (or 'done'): ").strip().lower()
        if symptom == 'done' or symptom == '':
            break
        if symptom:
            entered_symptoms.append(symptom)

    if not entered_symptoms:
        print("⚠️  No symptoms entered. Cannot diagnose.")
        return

    print(f"\nYou entered: {', '.join(entered_symptoms)}\n")
    print("="*50)
    print("🔍 Diagnosis Results:")
    print("="*50)

    best_matches = []
    for disease_name, db_symptoms, treatments in crop_disease_db:
        if disease_name == "Healthy" and entered_symptoms:
            continue  

      
        matched_count = sum(1 for s in entered_symptoms if any(keyword in s or s in keyword for keyword in db_symptoms))
        total_user_symptoms = len(entered_symptoms)

        if matched_count > 0:
            match_percentage = (matched_count / total_user_symptoms) * 100
            best_matches.append((match_percentage, matched_count, disease_name, db_symptoms, treatments))

  
    best_matches.sort(reverse=True, key=lambda x: (x[0], x[1]))

    if not best_matches:
        print("❌ No matching diseases found in the database.")
        print("   → This could be a nutrient deficiency, pest damage, or a rare disease.")
        print("   → Recommendation: Consult a local agronomist or send photos to a plant clinic.")
    else:
       
        for i, (percentage, count, name, symptoms, treatments) in enumerate(best_matches[:3]):
            confidence = "High" if percentage >= 75 else "Medium" if percentage >= 50 else "Low"
            print(f"\n#{i+1} Possible Match → {name}")
            print(f"   Confidence: {confidence} ({count}/{len(entered_symptoms)} symptoms match) ≈ {percentage:.0f}%")
            print(f"   Known symptoms: {', '.join(symptoms)}")
            print(f"   💡 Recommended actions:")
            for action in treatments:
                print(f"      • {action}")

        if len(best_matches) > 3:
            print(f"\n... and {len(best_matches)-3} other less likely possibilities.")

  
    if best_matches and best_matches[0][0] < 50:
        print("\nℹ️  Note: Low confidence match. The plant might still be healthy or affected by non-disease issues (e.g., overwatering, nutrient deficiency).")

    print("\n" + "="*50)
    print("Always confirm with a local expert before applying chemicals!")
    print("==================================================")

if __name__ == "__main__":
    check_symptoms()