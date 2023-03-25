class Airport:
    def __init__(self, code, city, country, continent ) -> None:
        self.code = code
        self.city = city
        self.country = country
        self.continent = continent
    
    def __repr__(self) -> str:
        
        return f"{self.code}, ({self.city}, {self.country})"

    def getCode(self) -> str:
        return self.code()
    
    def getCity(self) -> str:
        return self.city
    
    def getcountry(self) -> str:
        return self.country
    
    def getcontinent(self) -> str:
        return self.getcontinent
    
    def setCity(self, city):
        self.city = city

    def setCountry(self, country):
        self.country = country           
    
    def setContinent(self, continent):
     self.continent = continent

