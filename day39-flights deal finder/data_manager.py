import requests
from pprint import pprint
from requests.auth import HTTPBasicAuth

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.sheety_api = "https://api.sheety.co/deff698b4eedb44e4b46aee20215f5b9/flightDeals/prices"

        self.sheety_response = requests.get(url=self.sheety_api)
        self.sheet_data = self.sheety_response.json()


    def update(self, data):
        for i in data:
            self.Object_ID = i["id"]
            self.sheety_endpoint = f"https://api.sheety.co/deff698b4eedb44e4b46aee20215f5b9/flightDeals/prices/{self.Object_ID}"
            self.new_itadata = {
                "price":{
                    "iataCode": i["iataCode"]
                }
            }
            # self.header = {
            #     "Authorization": "aGFyc2h2c2luZ2g6bXJncmVlbjk0MTY"
            # }
            

            self.response = requests.put(url = self.sheety_endpoint, json = self.new_itadata)
            print(self.response.text)
