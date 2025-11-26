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
        self.__fones = list[Fone] = []
        self.__favorited = False
    
    def __str__(self):
        prefixo = "-"
        if self.__favorited:
            prefixo = "@"
        
        telefones = ", ".join(f"{x}:{y}" for x, y in self.__fones)

        return f"{prefixo} {self.__name} [{telefones}]"

    def addFone(self, id: str, number: str):
        self.__fones.append((id, number))

    def rmFone(self, index: int):
        self.__fones.remove(index)

    def toogleFavorited(self):
        self.__favorited = not self.__favorited

def main():
    

    
    
    

    
        

    

