from pprint import pprint

import os
from dotenv import load_dotenv
import requests

load_dotenv()

SERP_API_ENDPOINT = os.getenv("SERP_API_ENDPOINT")

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = os.environ["SERP_API_KEY"]

    def check_flights(self, origin_city_code, destination_city_code, departure_date, return_date):
        params = {
            "api_key": self._api_key,
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "outbound_date": departure_date,
            "return_date": return_date,
        }

        response = requests.get(url=SERP_API_ENDPOINT, params=params)
        response.raise_for_status()
        data = response.json()

        pprint(data)