import requests
from dotenv import load_dotenv
import os

load_dotenv()

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.username = os.getenv("SHEETY_USERNAME")
        self.password = os.getenv("SHEETY_PASSWORD")

        self.sheety_endpoint = os.getenv("SHEETY_ENDPOINT")

        self.sheety_response = requests.get(self.sheety_endpoint, auth=(self.username, self.password))
        self.sheety_json = self.sheety_response.json()



    def get_destination_data(self):
        return self.sheety_json["prices"]

