from Flight import *
from Airport import *

class Aviation:
    def __init__(self) -> None:
        self._allAirports = [] # any type
        self._allFlights = {}
        self._allCountries = {}
   


    def loadData(self, airportFile: str, flightFile: str, countriesFile: str):
        allCountries = {}
        with open(airportFile, "r") as airportf:
            key, value = [line.strip(" ").split(",") for line in airportf.readlines()]
            allCountries = allCountries.update(key, value)
        self._allCountries = allCountries

        with open(airportFile) as airportf:
            flightNo, country, city = [line.strip(" ").split(",") for line in airportf.readlines()]
            airport = airport(flightNo, country, city, allCountries[country])



        with open(flightFile) as flightf:
            flightNo, origAirport, destAirport= [line.strip(" ").split(",") for line in flightf.readlines()]
            flight  = flight(flightNo, origAirport, destAirport)





        # with open(flightFile, "r") as flightf:
        #     with opeen(countriesFile, "r") as countriesf: