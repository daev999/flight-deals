import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

SHEETY_PRICES_ENDPOINT = os.getenv("SHEETY_ENDPOINT")

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self._username = os.getenv("SHEETY_USERNAME")
        self._password = os.getenv("SHEETY_PASSWORD")
        self._authorization = HTTPBasicAuth(self._username, self._password)
        self.destination_data = {}

    def get_destination_data(self):
        sheety_response = requests.get(SHEETY_PRICES_ENDPOINT, auth=self._authorization)
        data = sheety_response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_lowest_price(self, row_id, new_price):
        body = {
            "price": {
                "lowestPrice": new_price
            }
        }
        response = requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{row_id}", json=body, auth=self._authorization)

        response.raise_for_status()