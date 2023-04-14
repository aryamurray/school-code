# Here is the Aiport class that has everything to do with the invididual airports

class Airport: # This constructor instantiates the basic info about an airport
    def __init__(self, code, city, country, continent ) -> None:
        self.code = code
        self.city = city
        self.country = country
        self.continent = continent
    # String Representation
    def __repr__(self) -> str:
        
        return f"{self.code} ({self.city}, {self.country})"


    # Literally all of the following are just methods of returning properties.
    def getCode(self) -> str:
        return self.code
    
    def getCity(self) -> str:
        return self.city
    
    def getCountry(self) -> str:
        return self.country
    
    def getContinent(self) -> str:
        return self.continent
    
    def setCity(self, city):
        self.city = city

    def setCountry(self, country):
        self.country = country           
    
    def setContinent(self, continent):
        self.continent = continent

