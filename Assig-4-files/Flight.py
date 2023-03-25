from Airport import *

class Flight:
   def __init__(self, flightNo, origAirport, destAirport) -> None:
      if isinstance(origAirport, Airport) == False or isinstance(destAirport, Airport) == False:
         raise ValueError("The origin and destination arguments must be Airport objects")
      
      self.flightNo = flightNo
      self.origAirport = origAirport
      self.destAirport = destAirport

    def __repr__(self) -> str:
        return f"Flight({self.flightNo}): {self.origAirport.getCity()} -> {destinationCity} {[domestic]/[international]}"