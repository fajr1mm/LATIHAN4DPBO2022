class person:

    def __init__(self):
        super().__init__()
        self.__nameP = ""
        self.__idPerson = ""
        self.__gender = ""
    
    # class constructors
    def setperson(self, nameP = "", idPerson = "", gender = ""):
        self.__nameP = nameP
        self.__idPerson = idPerson
        self.__gender = gender        
        
    # getter and setter
    def setnameP(self, nameP):
        self.__nameP = nameP
    
    def getnameP(self):
        return self.__nameP
    
    def setIdPerson(self, idPerson):
        self.__idPerson = idPerson
    
    def getIdPerson(self):
        return self.__idPerson

    def setgender(self, gender):
        self.__gender = gender
    
    def getgender(self):
        return self.__gender
    
    # sleep method 
    def sleep(self):
        print(self.__nameP + " isnt sleep....")