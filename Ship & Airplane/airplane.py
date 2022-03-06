from vehicle import vehicle

class airplane(vehicle):
    
    # class constructors
    def __init__(self, name = "", fuelType = "", maxPass = "", type = "", age = "", manucatOri = "", boeing = "", speed = "", firstFlight = ""):
        self.setVehicle(name, fuelType, maxPass, type, age, manucatOri)
        self.__boeing = boeing
        self.__speed = speed
        self.__firstFlight = firstFlight
        
    # getter and setter
    def setboeing(self, boeing):
        self.__boeing = boeing
    
    def getboeing(self):
        return self.__boeing
    
    def setspeed(self, speed):
        self.__speed = speed
    
    def getspeed(self):
        return self.__speed
    
    def setfirstFlight(self, firstFlight):
        self.__firstFlight = firstFlight
    
    def getfirstFlight(self):
        return self.__firstFlight

    
    # method for showing class
    def printAirplane(self):
        print("-------------------------------------------------")
        print("Ship                     : " + self.getname())
        print("Fuel Type                : " + self.getfuelType())
        print("Maximal Passenger        : " + self.getmaxPass())
        print("Type                     : " + self.gettype())
        print("Age                      : " + self.getage())
        print("Manufacture Origin       : " + self.getmanufactOri())
        print("Boeing                   : " + str(self.getboeing()))
        print("Speed                    : " + str(self.getspeed()) + "km/H")
        print("First Flight             : " + str(self.getfirstFlight()))
        self.Move()
        print("-------------------------------------------------")