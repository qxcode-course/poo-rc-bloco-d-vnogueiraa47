class Fone:
    def __init__(self, id: str, number: str):
        self.__id =  id
        self.__number = number

    def getId(self):
        return self.__id
    
    def getNumber(self):
        return self.__number
    
    def __str__(self):
        return f"{self.__id}:{self.__number}"
    
    def isValid(self):
        n = "0123456789()."

        for x in self.__number:
            if x not in n:
                raise Exception (f"fail: invalid number")
            return False


class Contact:
    def __init__(self, name: str):
        self.__name = name
    
    def __str__(self):
        return f"- {self.__name} []"

    def addFone(self, id: str, number: str):
        IndexError
    
    def rmFone(self, index: int):
        IndexError
    
    def toogleFavorited(self):
        IndexError
    
    def isFavorited(self):
        return False

    
    
    

    
        

    

