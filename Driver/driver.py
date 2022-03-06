from person import person
from job import job

class driver(person, job):

    def __init__(self):
        super().__init__()
        self.__lisenceId = ""
        self.__activeUntil = ""
        self.__vehicleType = ""
    
    # class constructors
    def __init__(self, nameP = "", idPerson = "", gender = "", nameJ = "", idJob = "", company = "", position = "", lisenceId = "", activeUntil = "", vehicleType = ""):
        self.setperson(nameP, idPerson, gender)
        self.setjob(nameJ, idJob, company, position)
        self.__lisenceId = lisenceId
        self.__activeUntil = activeUntil
        self.__vehicleType = vehicleType
        
    # getter and setter
    def setlisenceId(self, lisenceId):
        self.__lisenceId = lisenceId
    
    def getlisenceId(self):
        return self.__lisenceId
    
    def setactiveUntil(self, activeUntil):
        self.__activeUntil = activeUntil
    
    def getactiveUntil(self):
        return self.__activeUntil
    
    def setvehicleType(self, vehicleType):
        self.__vehicleType = vehicleType
    
    def getvehicleType(self):
        return self.__vehicleType

    
    # method for showing class
    def printDriver(self):
        print("-------------------------------------------------")
        print("Name                     : " + self.getnameP())
        print("ID                       : " + self.getIdPerson())
        print("Gender                   : " + self.getgender())
        print("Job                      : " + self.getnameJ())
        print("ID Job                   : " + self.getIdJob())
        print("Company                  : " + self.getcompany())
        print("Position                 : " + self.getposition())
        print("Lisence ID               : " + str(self.getlisenceId()))
        print("Activated                : " + str(self.getactiveUntil()))
        print("Vehicle Type             : " + str(self.getvehicleType()))
        self.sleep()
        print("-------------------------------------------------")