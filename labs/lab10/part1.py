# Define class Fruit  
class Fruit():  
    def __init__(self):  
        self.shape = ""
        self.colour = ""
          
  
    def canBePhone(self):  
        return "fruits can't be phones..."
  
# Define class Banana  
class Banana(Fruit):  
    def __init__(self):  
        pass
  
    def canBePhone(self):  
        return "Bananas can be phones!"
  

apple=Fruit()  
print(apple.canBePhone())  
banana=Banana()  
print(banana.canBePhone()) 