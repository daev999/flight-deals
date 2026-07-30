import os
from dotenv import load_dotenv
import requests

load_dotenv()

SERP_API_ENDPOINT = os.getenv("SERP_API_ENDPOINT")

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = os.environ["SERP_API_KEY"]

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        params = {
            "api_key": self._api_key,
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "outbound_date": from_time.strftime("%Y-%m-%d"),
            "return_date": to_time.strftime("%Y-%m-%d"),
            "engine": "google_flights",
            "type": "1",
            "adults": "1",
            "currency": "GBP",
        }

        response = requests.get(url=SERP_API_ENDPOINT, params=params)

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            return None

        data = response.json()
        if "error" in data:
            print(f"API error: {data['error']}")
            return None
        return data

