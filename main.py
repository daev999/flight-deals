from pprint import pprint
import requests_cache
from data_manager import DataManager
from datetime import datetime, timedelta
from flight_search import FlightSearch
from flight_data import FlightData

print("Program started")

requests_cache.install_cache(
    "flight_cache",
    urls_expire_after={
        "*.sheety.co*": requests_cache.DO_NOT_CACHE, # Never cache Sheety.
        "*": 3600,                                   # Cache everything else for 1 hour.
    }
)

# ==================== Talk to Sheety ====================
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
# pprint(sheet_data)

# ==================== Set the Dates ====================
today = datetime.now()

tomorrow = today + timedelta(days=1)
six_month_from_today = today + timedelta(days=180)

# ==================== Do a Flight Search ====================
flight_search = FlightSearch()


flights = flight_search.check_flights(
    origin_city_code="LHR",
    destination_city_code=sheet_data[0]["iataCode"],
    from_time=tomorrow,
    to_time=six_month_from_today,
)

first_best_flight = flights["best_flights"][0]

cheapest_flight = None
for flight in flights["best_flights"]:
    if cheapest_flight is None:
        cheapest_flight = flight
    elif flight["price"] < cheapest_flight["price"]:
        cheapest_flight = flight

flight_data = FlightData(
    price=cheapest_flight["price"],
    origin_airport=cheapest_flight["flights"][0]["departure_airport"]["id"],
    destination_airport=cheapest_flight["flights"][0]["arrival_airport"]["id"],
    out_date=cheapest_flight["flights"][0]["departure_airport"]["time"],
    return_date=cheapest_flight["flights"][-1]["arrival_airport"]["time"],
)

print(f"Flight price: {flight_data.price}")
print(f"Spreadsheet price: {sheet_data[0]['lowestPrice']}")

if flight_data.price < sheet_data[0]["lowestPrice"]:
    print(f"Lower price found for {sheet_data[0]['city']}!")

    data_manager.update_lowest_price(row_id=sheet_data[0]["id"], new_price=flight_data.price)