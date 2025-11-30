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
        valid_chars = "0123456789()."
        for char in self.__number: 
            if char not in valid_chars:
                raise ValueError("fail: invalid number")
        return True


class Contact:
    def __init__(self, name: str):
        self.__name = name
        self.__fones: list[Fone] = []
        self.__favorited = False
    
    def __str__(self):
        prefixo = "-"
        if self.__favorited:
            prefixo = "@"
        
        telefones = ", ".join(str(fone) for fone in self.__fones)

        return f"{prefixo} {self.__name} [{telefones}]"

    def addFone(self, id: str, number: str):
        fone = Fone(id, number)
        if fone.isValid():
            self.__fones.append(fone)

    def rmFone(self, index: int):
        self.__fones.pop(index)

    def toogleFavorited(self):
        self.__favorited = not self.__favorited
    
    def GetFones(self):
        return self.__fones
    
    def getName(self):
        return self.__name
    
    def setName(self, name: str):
    
        self.__name = name  
    
    
def main():

    contact = Contact("")

    while True:
        line = input()
        print("$" + line)
        args = line.split()
        command = args[0]

        if command == "end":
            break
        elif command == 'init':
            nome = args[1]
            contact = Contact(nome)
        elif command == "show":
            print(contact)
        elif command == "add":
            try:
                label = args[1]
                number = args[2]
                contact.addFone(label, number) 

            except ValueError as e:
                print(e)
            
        elif command == "rm":
            x = int(args[1])
            contact.rmFone(x)
        elif command == "tfav":
            contact.toogleFavorited()

main()
    

    
    
    

    
        

    

