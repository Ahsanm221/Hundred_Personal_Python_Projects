import requests
import os
from datetime import datetime

APP_ID = os.environ["APP_ID_EXERCISE"]
APP_KEY = os.environ["APP_KEY_EXERCISE"]
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.environ["SHEET_ENDPOINT"]

exercise_input = input("Which exercises did you do today?  ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

parameters = {
    "query": exercise_input,
    "gender": "male",
    "weight_kg": 88,
    "height_cm": 182.82,
    "age": 24,
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()
today = datetime.now().strftime("%d/%m/%Y")
now = datetime.now().strftime("%H:%M:%S")

bearer_headers = {"Authorization": f"Bearer {os.environ['TOKEN']}"}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today,
            "time": now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs, headers=bearer_headers)
