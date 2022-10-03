import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth
import os

AGE = 29
HEIGHT_CM = 180.64
WEIGHT_KG = 72.5
GENDER = "male"
QUERY = input("what exercises you did ?")
NAME = "Harsh"
EMAIL = "mail.harshvsingh@gmail.com"
APP_ID = "74ac6afd"
APP_KEY = "477efb92da0491b467695eeab2c98010"
USERNAME: "harshvsingh"
PASSWORD = "mrgreen9416"
EXERCISE_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_params = {
    "query":QUERY,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
headers = {
    "x-app-id":APP_ID,
    "x-app-key": APP_KEY,

}

response = requests.post(url = EXERCISE_endpoint, json= exercise_params, headers=headers)
result = response.json()


sheet_endpoint = "https://api.sheety.co/deff698b4eedb44e4b46aee20215f5b9/myWorkouts/workouts"
TODAY_DATE = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": TODAY_DATE,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    #sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    #print(sheet_response.text)

auth = {
    "Username": "harshvsingh",
    "Password": "mrgreen9416"
}

sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, auth= HTTPBasicAuth("harshvsingh","mrgreen9416"))
print(sheet_response.text)

# we have to keep the auth token and API key hidden for security puposes.
# We can store these things as environment variables.
#we do this by typing - export (name of the variable)=(apikey/auth_token)
# the import os and in place of the whole key or token , use - os.environ.get("name of the variable")