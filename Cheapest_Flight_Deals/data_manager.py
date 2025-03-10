import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/c1b5ed86ad51220393a133fbc7a295ab/flightDeals/prices"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/c1b5ed86ad51220393a133fbc7a295ab/flightDeals/users"
TOKEN = {"Authorization": "Bearer LKAJaldjflj12434411109"}


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=TOKEN)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}", json=new_data, headers=TOKEN)
            print(response.text)

    def get_customer_emails(self):
        customers_endpoint = SHEETY_USERS_ENDPOINT
        response = requests.get(url=customers_endpoint, headers=TOKEN)
        data = response.json()
        print(data)
        self.customer_data = data["users"]
        return self.customer_data