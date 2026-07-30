from pprint import pprint
from time import strftime
import requests_cache
from data_manager import DataManager
from datetime import datetime, timedelta
from flight_search import FlightSearch

requests_cache.install_cache("flight_cache", expires_after=3600)

today = datetime.now()
tomorrow = (today + timedelta(days=1)).strftime("%Y-%m-%d")
six_month_from_today = (today + timedelta(days=180)).strftime("%Y-%m-%d")

return_date = (today + timedelta(days=7)).strftime("%Y-%m-%d")

data_manager = DataManager()
flight_search = FlightSearch()

sheet_data = data_manager.get_destination_data()

flight_search.check_flights(
    origin_city_code="LON",
    destination_city_code=sheet_data[0]["iataCode"],
    departure_date=tomorrow,
    return_date=return_date,
)

pprint(sheet_data)