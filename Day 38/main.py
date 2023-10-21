import requests
import datetime
import os

date = datetime.datetime.now()

APPID = os.environ["APPID"]
APIKEY = os.environ["APIKEY"]

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutritionix_headers = {
    "x-app-id": APPID,
    "x-app-key": APIKEY,
}

user_input = input("Tell me which exercise you did?\n")


nutritionix_params = {
    "query": user_input,
    "gender": "male",
    "weight_kg": 66,
    "height_cm": 177,
    "age": 18
}

response = requests.post(nutritionix_endpoint, nutritionix_params, headers=nutritionix_headers)
response.raise_for_status()
data = response.json()["exercises"][0]

formatted_date = date.strftime('%d/%m/%Y')
formatted_time = date.strftime('%H:%M:%S')
exercise_name = data["name"]
duration = data["duration_min"]
calories = data["nf_calories"]

print(formatted_date)
print(formatted_time)
print(exercise_name)
print(duration)
print(calories)

new_stats = {
    "workout": {
        "date": formatted_date,
        "time": formatted_time,
        "exercise": exercise_name,
        "duration": duration,
        "calories": calories
    }
}

TOKEN = os.environ["TOKEN"]

sheety_header = {
    "Authorization": f"Bearer {TOKEN}"
}

sheety_endpoint = f"https://api.sheety.co/bbb739425f199d38553b9be72b138414/workoutTracing/workouts"

sheety_response = requests.post(sheety_endpoint, json=new_stats, headers=sheety_header)
sheety_response.raise_for_status()
