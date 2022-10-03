from data_manager import *

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        self.data = DataManager().sheet_data
        self.alldata= self.data["prices"]
    def ita_replace(self):
        for i in self.alldata:
            if len(i["iataCode"]) == 0:
                i["iataCode"] = "TESTING"
            
        return self.alldata

        

