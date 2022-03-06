class job:

    def __init__(self):
        super().__init__()
        self.__nameJ = ""
        self.__idJob= ""
        self.__company = ""
        self.__position = ""
    
    # class constructors
    def setjob(self, nameJ = "", idJob= "", company = "", position = ""):
        self.__nameJ = nameJ
        self.__idJob= idJob
        self.__company = company
        self.__position = position         
        
    # getter and setter
    def setnameJ(self, nameJ):
        self.__nameJ = nameJ
    
    def getnameJ(self):
        return self.__nameJ
    
    def setIdJob(self, idJob):
        self.__idJob= idJob
    
    def getIdJob(self):
        return self.__idJob

    def setcompany(self, company):
        self.__company = company
    
    def getcompany(self):
        return self.__company
    
    def setposition(self, position):
        self.__position = position
    
    def getposition(self):
        return self.__position