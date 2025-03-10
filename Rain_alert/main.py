import requests

# api needs a subscription
api_key = "39a39fcbc05cf9b03f45545738667dc7"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"

weather_params = {
    "lat": 33.684422,
    "lon": 73.047882,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
print(response.status_code)
weather_data = response.json()

weather_slice = weather_data["hourly"][:12]
will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella.")

# for i in range(11):
#     if weather_data["hourly"][i]["weather"][i]["id"] < 700:
#         print("Bring an umbrella.")

# You can use twilio for sending text, refer to day 35 on how to use its classes.
