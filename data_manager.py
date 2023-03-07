import os
import requests

SHEETY_USERNAME = "c63e2661dc2e38ae22ff20e78e59a1b3"
SHEETY_PROJECT_NAME = "flightDeals"
SHEETY_SHEET_NAME = "prices"
SHEETY_TOKEN = os.environ.get("ENV_SHEETY_TOKEN")

sheeety_endpoint = f"https://api.sheety.co/{SHEETY_USERNAME}/{SHEETY_PROJECT_NAME}/{SHEETY_SHEET_NAME}"

sheety_headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

class DataManager:
    def __init__(self):
        self.sheety_data = []

    def getData(self):
        response = requests.get(url=sheeety_endpoint, headers=sheety_headers)
        self.sheety_data = response.json()['prices']
        return self.sheety_data

    def updateIATACode(self):
        for record in self.sheety_data:
            record_update = {
                "price": {
                    "iataCode": record["iataCode"]
                }
            }
            r = requests.put(url=f"{sheeety_endpoint}/{record['id']}", headers=sheety_headers, json=record_update)
            r.raise_for_status()