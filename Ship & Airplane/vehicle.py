class vehicle:

    def __init__(self):
        super().__init__()
        self.__name = ""
        self.__fuelType = ""
        self.__maxPass = ""
        self.__type = ""
        self.__age = ""
        self.__manufactOri = ""
    
    # class constructors
    def setVehicle(self, name = "", fuelType = "", maxPass = "", type = "", age = "", manufactOri = ""):
        self.__name = name
        self.__fuelType = fuelType
        self.__maxPass = maxPass        
        self.__type = type
        self.__age = age
        self.__manufactOri = manufactOri
        
    # getter and setter
    def setname(self, name):
        self.__name = name
    
    def getname(self):
        return self.__name
    
    def setfuelType(self, fuelType):
        self.__fuelType = fuelType
    
    def getfuelType(self):
        return self.__fuelType

    def setmaxPass(self, maxPass):
        self.__maxPass = maxPass
    
    def getmaxPass(self):
        return self.__maxPass
    
    def settype(self, type):
        self.__type = type
    
    def gettype(self):
        return self.__type
    
    def setage(self, age):
        self.__age = age
    
    def getage(self):
        return self.__age

    def setmanufactOri(self, manufactOri):
        self.__manufactOri = manufactOri
    
    def getmanufactOri(self):
        return self.__manufactOri
    
    # move method 
    def Move(self):
        print(self.__name + " will move....")