from vehicle import vehicle

class ship(vehicle):

    def __init__(self):
        super().__init__()
        self.__portRegist = ""
        self.__lenght = ""
        self.__owner = ""
    
    # class constructors
    def __init__(self, name = "", fuelType = "", maxPass = "", type = "", age = "", manucatOri = "", portRegist = "", lenght = "", owner = ""):
        self.setVehicle(name, fuelType, maxPass, type, age, manucatOri)
        self.__portRegist = portRegist
        self.__lenght = lenght
        self.__owner = owner
        
    # getter and setter
    def setportRegist(self, portRegist):
        self.__portRegist = portRegist
    
    def getportRegist(self):
        return self.__portRegist
    
    def setlenght(self, lenght):
        self.__lenght = lenght
    
    def getlenght(self):
        return self.__lenght
    
    def setowner(self, owner):
        self.__owner = owner
    
    def getowner(self):
        return self.__owner

    
    # method for showing class
    def printShip(self):
        print("-------------------------------------------------")
        print("Ship                     : " + self.getname())
        print("Fuel Type                : " + self.getfuelType())
        print("Maximal Passenger        : " + self.getmaxPass())
        print("Type                     : " + self.gettype())
        print("Age                      : " + self.getage())
        print("Manufacture Origin       : " + self.getmanufactOri())
        print("Port Register            : " + str(self.getportRegist()))
        print("Lenght                   : " + str(self.getlenght()))
        print("Owner                    : " + str(self.getowner()))
        self.Move()
        print("-------------------------------------------------")