import requests
import os
from flight_data import FlightData

kiwi_api_key = os.environ.get("KIWI_API_KEY")
flights_search_endpoint = "https://tequila-api.kiwi.com"
CURR = "USD"
FLIGHT_TYPE = "round"
ONE_FOR_CITY = 1
NIGHTS_IN_DST_FROM = 3
NIGHTS_IN_DST_TO = 15


class FlightSearch:
    def getIataCode(self,city_name):
        location_endpoint = f"{flights_search_endpoint}/locations/query"
        headers = {"apikey": kiwi_api_key,}
        query = {"term": city_name}
        response = requests.get(url=location_endpoint,headers=headers,params=query)
        response.raise_for_status()
        iataCode = response.json()["locations"][0]["code"]
        return iataCode

    def findPrice(self,origin_city_iataCode, destination_city_iataCode, date_from, date_to):
        search_endpoint = f"{flights_search_endpoint}/v2/search"
        headers = {"apikey": kiwi_api_key,}
        # query = {
        #     "fly_from": origin_city,
        #     "fly_to": iataCode,
        #     "date_from": date_from.strftime("%d/%m/%Y"),
        #     "date_to": date_to.strftime("%d/%m/%Y"),
        #     "flight_type": "round",
        #     "one_for_city": 1,
        #     "curr": "USD",
        # }
        date_f = date_from.strftime("%d/%m/%Y")
        date_t = date_to.strftime("%d/%m/%Y")
        search_endpoint_params = f'{search_endpoint}?fly_from={origin_city_iataCode}&fly_to={destination_city_iataCode}&date_from={date_f}&date_to={date_t}&nights_in_dst_from={NIGHTS_IN_DST_FROM}&nights_in_dst_to={NIGHTS_IN_DST_TO}&flight_type={FLIGHT_TYPE}&one_for_city={ONE_FOR_CITY}&max_stopovers=0&curr={CURR}'
        response = requests.get(url=search_endpoint_params,headers=headers)
        response.raise_for_status()
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_iataCode}.")
            return None
        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_code=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_code=data["route"][0]["flyTo"],
            departure_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.origin_city}->{flight_data.destination_city}: ${flight_data.price} on {flight_data.departure_date}")
        return flight_data





