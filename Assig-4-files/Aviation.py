# from Flight import *
# from Airport import *

class Aviation:
    def __init__(self) -> None:
        pass
   


    def loadData(self, airportFile: str, flightFile: str, countriesFile: str):
        with open(airportFile, "r") as airportf:
            contents = [line.strip(" ").split(",") for line in airportf.readlines()]
            print(contents)


        # with open(flightFile, "r") as flightf:
        #     with opeen(countriesFile, "r") as countriesf: