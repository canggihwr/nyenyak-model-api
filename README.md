# Nyenyak-model-backend

### Prerequisites

- Python 3.x
- pip (package installer for Python)

### 1. Create a virtual environment (optional)
```
python -m venv venv
```
### 2. Install dependencies
```
pip install -r requirements.txt
```
### 3. Run the Flask app
```
python nyenyak.py
```
Use the `/prediction` endpoint for making predictions. Send a POST request with JSON data to get predictions.
```
{
  "Age": 27,
  "Sleep_Duration": 6.1,
  "Sleep_Quality": 6,
  "Physical_Activity_Level": 42,
  "Stress_Level": 6,
  "Heart_Rate": 77,
  "Daily_Steps": 4200,
  "Gender_Male": 1,
  "BMI_Category_Obese": 0,
  "BMI_Category_Overweight": 1,
  "BP_Category_Normal": 0,
  "BP_Category_Stage 1": 1,
  "BP_Category_Stage 2": 0
}
```
