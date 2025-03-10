from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
import datetime


data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "ISB"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = (datetime.datetime.now() + datetime.timedelta(days=75)).strftime("%d/%m/%Y")
six_months_after = (datetime.datetime.now() + datetime.timedelta(days=180)).strftime("%d/%m/%Y")

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months_after
    )
    if flight is None:
        continue

    if flight.price < destination["lowestPrice"]:

        users = data_manager.get_customer_emails()
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]
        print(emails, names)

        message = f"Low price alert! Only £{flight.price} to fly from " \
                  f"{flight.origin_city}-{flight.origin_airport} to {flight.destination_city}" \
                  f"-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
            print(message)

        notification_manager.send_emails(emails, message)
