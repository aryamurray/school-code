# PART 1

# class Fruit():
#     def __init__(self, clr = "", shp = "", tst = ""):
#         self._colour = clr
#         self._shape = shp
#         self._taste = tst

#     def descriptor(self):
#         return self._colour + "," + self._shape + "," + self._taste
    
# class Banana(Fruit):
#     def __init__(self, clr="", shp="", tst=""):
#         super().__init__(clr, shp, tst)

# class Apple(Fruit):
#     def __init__(self, clr="", shp="", tst="", type = ""):
#         super().__init__(clr, shp, tst)
#         self._type = type

#     def setType(self, value):
#         self._type = value

#     def descriptor(self):
#         return super().descriptor() + "," + self._type



# afruit = Fruit("green", "round", "sweet")
# print("A fruit:", afruit.descriptor())
# bn = Banana("yellow", "long", "soft and sweet")
# print("A banana:", bn.descriptor())

# app1 = Apple("red", "round", "sweet and crunchy")
# print("An apple:", app1.descriptor())
# app1.setType("Gala")
# print("A particular apple:", app1.descriptor())


##############################################################################



#Part 2


class Automobile():
    def __init__(self, ndoors = 0, clr = "") -> None:
        self._doors = ndoors
        self._colour = clr

    def printDoors(self):
        return "Number of doors is " + str(self._doors)
    
    def printColour(self):
        return "Colour is: " + self._colour
    
    def display(self):
        return "Car is:" + str(self._doors) + " doors," +self._colour
    
class sportsCar(Automobile):
    def __init__(self, ndoors: int, clr: str, eng: int) -> None:
        super().__init__(ndoors, clr)
        self._engine = eng

    def display(self):
        return "Car is:" + str(self._doors) + " doors," + self._colour + ", with " + str(self._engine) + " hp"
    

ferrari = sportsCar(2, "red", 450 )
print(ferrari.display())