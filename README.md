🌱 Crop Disease Symptom Checker

This project is a simple yet effective command-line tool that helps farmers, students, and plant enthusiasts identify possible plant diseases based on visible symptoms.
The tool compares user-entered symptoms with a small database of common crop diseases and provides:

✅ Disease name
✅ Confidence score
✅ Matching symptoms
✅ Suggested treatments


---

📌 Features

Interactive CLI input (one symptom per line)

Matches symptoms to a built-in disease database

Shows top 3 most likely diseases with confidence levels

Provides actionable suggestions and treatments

Handles “no match found” scenarios gracefully

Includes detection for healthy plants



---

🗂 Disease Database Included

The tool can identify the following plant diseases:

Early Blight (Tomato)

Late Blight (Tomato)

Powdery Mildew (Various crops)

Mosaic Virus (Various crops)

Healthy (no symptoms)


Each disease contains:

A list of common symptoms

Recommended treatments



---

🚀 How to Run the Program

1. Clone or download the script

git clone <your repo link>
cd crop-disease-checker

2. Run the Python script

python3.13 crop_checker.py

OR

python3.13 crop_checker.py


---

🧪 How It Works

1. You enter symptoms one by one (example: brown spots, yellow halo, wilting, etc.)


2. Type done when finished.


3. The program compares your inputs with known symptoms in the database.


4. It ranks diseases by:

Percentage of symptoms matched

Number of matched symptoms



5. The top results are shown with confidence levels.




---

📝 Example Usage

🌱 Welcome to the Crop Disease Symptom Checker! 🌱
Describe what you see on your plant (one symptom per line).
Type 'done' when finished.

Enter symptom: brown spots
Enter symptom: rings
Enter symptom: done

Output:

#1 Possible Match → Early Blight (Tomato)
Confidence: High (2/2 symptoms match) ≈ 100%
Known symptoms: brown spots, yellow halo, rings, on leaves
💡 Recommended actions:
 • Remove affected leaves
 • Use organic fungicide (e.g., copper-based)
 • Improve air circulation
 • Avoid wetting leaves


---

📦 File Structure

crop-disease-checker/
│── crop_checker.py
│── README.md     ← (this file)


---

🛠 Requirements

No external libraries required — only Python 3.13


---

❤ Future Enhancements (Optional Ideas)

Add an image-based disease classifier using AI / CNN

Expand database to include more crops (wheat, rice, maize, etc.)

Build a mobile or web interface

Add pest/nutrient deficiency detection

Add probability scoring using NLP



Output:
<img width="1270" height="599" alt="image" src="https://github.com/user-attachments/assets/fb263c8c-bcb5-4fe8-b7c5-fd92962022ed" />


