from Flight import *
from Airport import *
#Here's where the magic happens. First is the constructor which gives us all our data
class Aviation:
    def __init__(self) -> None:
      self._allCountries = {}
      self._allAirports = {}
      self._allFlights = {}
   # Here are some basic methods to return properties
    def getAllAirports(self):
        return self._allAirports

    def getAllFlights(self):
        return self._allFlights 
    
    def getAllCountries(self):
        return self._allCountries
    
    def setAllAirpots(self, airports):
        self._allAirports = airports
    
    def setAllFlights(self, flights):
        self._allFlights = flights

    def setAllCountries(self, countries):
        self._allCountries = countries
    # One of the main methods which gathers all of the data
    def loadData(self, airportFile = "airports.txt", flightFile=  "flights.txt", countriesFile = "countries.txt"):
        allCountries = {}
        airports = {}
        flights = {}
        try:
            with open(countriesFile, "r", encoding="utf8") as countriesf:
                for line in countriesf:
                    line.strip()
                    country, continent = line.split(",")
                    country = country.strip()
                    continent = continent.strip().replace("\n", "")
                    allCountries.update({country:continent})
                self._allCountries = allCountries

            with open(airportFile, "r", encoding="utf8") as airportf:
                for line in airportf:
                    line.strip()
                    code, country, city = line.split(",")
                    code = code.strip()
                    country = country.strip()
                    city = city.strip()
                    value = [country, city]
                    airports.update({code:value})
                self._allAirports = airports

            with open(flightFile, "r", encoding="utf8") as flightf:
                for line in flightf:
                    line.strip()
                    flightNo, origAirport, destAirport = line.split(",")
                    flightNo = flightNo.strip()
                    origAirport = origAirport.strip()
                    destAirport = destAirport.strip()
                    flights.update({flightNo: [origAirport, destAirport]})
                self._allFlights = flights
            return True
        except:
            return False
    # Given a code, this method will return an airport
    def getAirportByCode(self, code):
        country = self._allAirports[code][0]
        city =  self._allAirports[code][1]
        continent = self._allCountries[country]
        return Airport(code, city, country, continent)
    # Will find all City Flights given a city
    def findAllCityFlights(self,city):
        allFlights = []
        for flightNo in self._allFlights:
            for airport in self._allFlights[flightNo]:
                    if self._allAirports[airport][1] == city:
                        origCode = self._allFlights[flightNo][0]
                        destCode = self._allFlights[flightNo][1]
                        origCity = self._allAirports[origCode][1]
                        destCity = self._allAirports[destCode][1]
                        origCountry = self._allAirports[origCode][0]
                        destCountry = self._allAirports[destCode][0]
                        origContinent = self._allCountries[origCountry]
                        destContinent = self._allCountries[destCountry]
                        allFlights.append(Flight(flightNo, Airport(origCode, origCity, origCountry, origContinent), Airport(destCode, destCity, destCountry, destContinent)))
                        continue
                    else:
                        pass
        return allFlights
    # Will find all the flights in a country given the country name
    def findAllCountryFlights(self, country):
        allFlights = []
        for flightNo in self._allFlights:
            for airport in self._allFlights[flightNo]:
                if self._allAirports[airport][0] == country: 
                    origCode = self._allFlights[flightNo][0]
                    destCode = self._allFlights[flightNo][1]
                    origCity = self._allAirports[origCode][1]
                    destCity = self._allAirports[destCode][1]
                    origCountry = self._allAirports[origCode][0]
                    destCountry = self._allAirports[destCode][0]
                    origContinent = self._allCountries[origCountry]
                    destContinent = self._allCountries[destCountry]
                    allFlights.append(Flight(flightNo, Airport(origCode, origCity, origCountry, origContinent), Airport(destCode, destCity, destCountry, destContinent)))
                    continue
                else:
                    pass
        return allFlights
    # Finds flights based on the flight number, returns flight object
    def findFlightByNo(self,flightNo):
        for flight in self._allFlights.keys():
            if flightNo == flight:
                origCode = self._allFlights[flightNo][0]
                destCode = self._allFlights[flightNo][1]
                origCity = self._allAirports[origCode][1]
                destCity = self._allAirports[destCode][1]
                origCountry = self._allAirports[origCode][0]
                destCountry = self._allAirports[destCode][0]
                origContinent = self._allCountries[origCountry]
                destContinent = self._allCountries[destCountry]
                return Flight(flight, Airport(origCode, origCity, origCountry, origContinent), Airport(destCode, destCity, destCountry, destContinent))  
        return -1
            # Finds flights between two airport object. Can search for one intermediary airport if there's no direct
    def findFlightBetween(self, origAirport: object, destAirport:object):
        for flight in self._allFlights:
            if origAirport.getCode() in self._allFlights[flight] and destAirport.getCode() in self._allFlights[flight]:
                return f"Direct Flight({flight}): {origAirport.getCode()} to {destAirport.getCode()}"
        possibleConnections = []
        for flight in self._allFlights:
            if origAirport.getCode() == self._allFlights[flight][0]:
                for secondFlight in self._allFlights:
                    if self._allFlights[secondFlight][0] == self._allFlights[flight][1]:
                        if self._allFlights[secondFlight][1] == destAirport.getCode():
                            possibleConnections.append(self._allFlights[flight][1])
        if len(possibleConnections) == 0:
            return -1
        else :
            return set(possibleConnections)
        # Attempts to find a reverse flight of the flight object inputted
    def findReturnFlight(self, firstFlight:object):
        if not isinstance(firstFlight, Flight):
            return -1
        firstFlightOrigin = firstFlight.getDestination().getCode()
        firstFlightDestination = firstFlight.getOrigin().getCode()
        for flightNo in self._allFlights:
            if self._allFlights[flightNo][0] == firstFlightOrigin and self._allFlights[flightNo][1] == firstFlightDestination:
                origCode = self._allFlights[flightNo][0]
                destCode = self._allFlights[flightNo][1]
                origCity = self._allAirports[origCode][1]
                destCity = self._allAirports[destCode][1]
                origCountry = self._allAirports[origCode][0]
                destCountry = self._allAirports[destCode][0]
                origContinent = self._allCountries[origCountry]
                destContinent = self._allCountries[destCountry]
                return Flight(flightNo, Airport(origCode, origCity, origCountry, origContinent), Airport(destCode, destCity, destCountry, destContinent))
        else:
            return -1
            # Finds flights across an ocean
    def findFlightsAcross(self,ocean):
        possibleFlights = []
        for flightNo in self._allFlights:
            origin = self._allFlights[flightNo][0]
            destination = self._allFlights[flightNo][1]
            originCountry = self._allAirports[origin][0]
            destinationCountry = self._allAirports[destination][0]
            originContinent = self._allCountries[originCountry]
            destinationContinent = self._allCountries[destinationCountry]
            if ocean == "Pacific":
                if originContinent == "Asia" and destinationContinent == "North America" or destinationContinent == "Asia" and originContinent == "North America":
                    possibleFlights.append(flightNo)
                if originContinent == "Asia" and destinationContinent == "South America" or destinationContinent == "Asia" and originContinent == "South America":
                    possibleFlights.append(flightNo)
                if originContinent == "Australia" and destinationContinent == "South America" or destinationContinent == "Australia" and originContinent == "South America":
                    possibleFlights.append(flightNo)
                if originContinent == "Australia" and destinationContinent == "North America" or destinationContinent == "Australia" and originContinent == "North America":
                    possibleFlights.append(flightNo)
            if ocean == "Atlantic":
                if originContinent == "Europe" and destinationContinent == "North America" or destinationContinent == "Europe" and originContinent == "North America":
                    possibleFlights.append(flightNo)
                if originContinent == "Europe" and destinationContinent == "South America" or destinationContinent == "Europe" and originContinent == "South America":
                    possibleFlights.append(flightNo)
                if originContinent == "Africa" and destinationContinent == "South America" or destinationContinent == "Africa" and originContinent == "South America":
                    possibleFlights.append(flightNo)
                if originContinent == "Africa" and destinationContinent == "North America" or destinationContinent == "Africa" and originContinent == "North America":
                    possibleFlights.append(flightNo)
        if len(possibleFlights) != 0: 
            return set(possibleFlights)
        return -1
            