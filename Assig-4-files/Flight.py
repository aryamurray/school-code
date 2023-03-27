from Airport import *

class Flight:
   def __init__(self, flightNo: str, origAirport: object, destAirport: object) -> None:
      if isinstance(origAirport, Airport) == False or isinstance(destAirport, Airport) == False:
         raise ValueError("The origin and destination arguments must be Airport objects")
      
      try:
         for char in flightNo:
            counter += 1
            if counter <= 3:
               if char != str:
                      raise ValueError("The flight number format is incorrect")
               if 3 < counter <=6:
                   if char != int:
                     raise ValueError("The flight number format is incorrect")
      except ValueError as err:
          print(err)
      
      self.flightNo = flightNo
      self.origAirport = origAirport
      self.destAirport = destAirport

   def __repr__(self) -> str:
      return f"Flight({self.flightNo}): {self.origAirport.getCity()} -> {self.destAirport.getcity()} [{self.}]"
   

   def __eq__(self, other: object) -> bool:
      if self.origAirport == other.origAirport and self.destAirport == other.destAirport:
         return True
      else:
         return False
      
   def getFlightNumber(self):
      return self.flightNo
   
   def getOrigin(self):
      pass #WHAT THE HELL>>>????

   def getDestination(self):
      pass

   def isDomesticFlight(self) -> bool:
      if self.origAirport.getcity() == self.destAirport.getcity():
         return True
      else:
         return False
      
   def setOrigin(self, origin: object):
      self.origAirport = origin

   def setDestination(self, destination: object):
      self.destAirport = destination


