from pprint import pprint
import requests_cache
from data_manager import DataManager
from datetime import datetime, timedelta
from flight_search import FlightSearch
from flight_data import find_cheapest_flight

print("Program started")

ORIGIN_CITY_IATA = "LHR"

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

for row in sheet_data:

    flights = flight_search.check_flights(
        origin_city_code=ORIGIN_CITY_IATA,
        destination_city_code=row["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today,
    )

    # Skip this city if no flights were returned
    if flights is None:
        continue

    print(f"Searching {row['city']}")

    cheapest_flight = find_cheapest_flight(
        flights,
        six_month_from_today.strftime("%Y-%m-%d")
    )

    print(f"{row['city']}: £{cheapest_flight.price}")
    print(f"Spreadsheet price: £{row['lowestPrice']}")

    if (
        cheapest_flight.price != "N/A"
        and cheapest_flight.price < row["lowestPrice"]
    ):
        print(f"Lower price found for {row['city']}!")

        data_manager.update_lowest_price(
            destination["id"],
            cheapest_flight.price
        )