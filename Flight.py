from Airport import *
# Here is the Fligh class that has everything to do with the flights
class Flight: # This constructor instantiates a flight object which takes a flight number and 2 airports as arguements
   def __init__(self, flightNo: str, origAirport: object, destAirport: object) -> None:
      if isinstance(origAirport, Airport) == False or isinstance(destAirport, Airport) == False:
         raise TypeError("the origin and destination must be airport objects")
     # basic error checking above for types
      try: # Error checking below for correct flight number 
         counter = 0
         for char in flightNo:
            counter += 1
            if counter <= 3:
               if char.islower() != char.islower():
                      raise ValueError("The flight number format is incorrect")
               if 3 < counter <=6:
                   if char != int:
                     raise ValueError("The flight number format is incorrect")
      except ValueError as err:
          print(err)
      #final step of instantiation
      self.flightNo = flightNo
      self.origAirport = origAirport
      self.destAirport = destAirport

      # This is also a string representation of an object 
   def __repr__(self) -> str:
      if self.isDomesticFlight() == True:
         return f"Flight({self.flightNo}): {self.origAirport.getCity()} -> {self.destAirport.getCity()} [domestic]"
      if self.isDomesticFlight() == False:
         return f"Flight({self.flightNo}): {self.origAirport.getCity()} -> {self.destAirport.getCity()} [international]"
   # This is for comparing two objects to another and returns a bool given if the origins and destinations match another flight
   def __eq__(self, other: object) -> bool:
      if isinstance(other, Flight):
         if self.getOrigin().getCode() == other.getOrigin().getCode() and self.getDestination().getCode() == other.getDestination().getCode():
            return True
            
      return False
      
      #The rest of the functions here just return the object properies
   def getFlightNumber(self):
      return self.flightNo
   
   def getOrigin(self):
      return self.origAirport

   def getDestination(self):
      return self.destAirport

   def isDomesticFlight(self) -> bool:
      if self.origAirport.getCountry() == self.destAirport.getCountry():
         return True
      else:
         return False
      
   def setOrigin(self, origin: object):
      self.origAirport = origin

   def setDestination(self, destination: object):
      self.destAirport = destination


