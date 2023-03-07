#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from datetime import datetime as dt, timedelta
from data_manager import DataManager
from notification_manager import NotificationManager
import pprint

ORIGIN_CITY_IATA = "SFO"

data_manager = DataManager()
sheet_data = data_manager.getData()
# print(sheet_data)

from flight_search import FlightSearch
flight_search = FlightSearch()
for record in sheet_data:
    if not record['iataCode']:
        record['iataCode'] = flight_search.getIataCode(record["city"])

data_manager.sheety_data = sheet_data
data_manager.updateIATACode()
# print(data_manager.sheety_data)

tomorrow = dt.now() + timedelta(days=1)
six_month_from_today = dt.now() + timedelta(days=180)

for record in sheet_data:
    # pprint.pprint(flight_search.findPrice(ORIGIN_CITY_IATA,record['iataCode'],tomorrow,six_month_from_today))
    flight_data = flight_search.findPrice(ORIGIN_CITY_IATA,record['iataCode'],tomorrow,six_month_from_today)
    try:
        if flight_data.price < record["lowestPrice"]:
            msg = NotificationManager()
            msg.send_message(f"Low price alert!Only ${flight_data.price} "\
                    f"to fly to {flight_data.destination_city} Chicago"\
                    f"on {flight_data.departure_date} - {flight_data.return_date}")
    except AttributeError:
        continue
    # print(flight_data.price)
    # msg = NotificationManager(flight_data)
    # msg.send_message()
    #
    # if flight_data.price < record['lowestPrice']:



