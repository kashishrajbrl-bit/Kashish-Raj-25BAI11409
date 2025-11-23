# 🌱 Crop Disease Symptom Checker

A simple, interactive command-line tool that helps farmers and gardeners identify common crop diseases based on observed symptoms and provides recommended management actions.

## Features

- Interactive symptom input (one per line)
- Fuzzy symptom matching against a built-in disease database
- Confidence scoring (High / Medium / Low) based on symptom match percentage
- Displays top 3 most likely diseases with treatment recommendations
- User-friendly output with clear formatting and emojis
- Includes a "Healthy" option and helpful warnings

## Currently Supported Diseases

| Disease                          | Crop(s)            |
|----------------------------------|--------------------|
| Early Blight                     | Tomato             |
| Late Blight                      | Tomato             |
| Powdery Mildew                   | Various crops      |
| Mosaic Virus                     | Various crops      |
| Healthy (no disease)             | All                |

## How It Works

The program compares user-entered symptoms (in natural language) against known symptom keywords for each disease. It calculates a match percentage and ranks results accordingly.

- **High Confidence**: ≥75% of your symptoms match
- **Medium Confidence**: 50–74%
- **Low Confidence**: <50%


