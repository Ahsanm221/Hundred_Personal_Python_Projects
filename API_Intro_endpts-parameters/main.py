import requests
from datetime import datetime
import smtplib
# import time

MY_LAT = 33.684422
MY_LONG = 73.047882
MY_EMAIL = "gorbapyo444@gmail.com"
PASSWORD = "ddnmynrijonbbeel"


def iss_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    latitude = float(data["iss_position"]["latitude"])
    longitude = float(data["iss_position"]["longitude"])
    if MY_LAT-5 < latitude < MY_LAT+5 and MY_LONG-5 < longitude < MY_LONG+5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    # Converting to +5 timezone
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) + 5
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) + 5

    time_now = datetime.now().hour
    print(sunrise, sunset, time_now)
    if sunset <= time_now or time_now <= sunrise:
        return True

# To check every minute, run program -> sleep 60s in an infinite loop
# while True:
#     time.sleep(60)


if iss_position() and is_night():
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(MY_EMAIL, PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg="Subject:Look up\n\nThe ISS is right above you in the sky"
    )
