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
    
class Agenda:
    def __init__(self):
        self.__contacts: dict[str,Contact] = {}
    
    def __find_pos_by_name(self, name: str) -> int:
        contacts_sorted = self.getContacts()

        for index, contact in enumerate(contacts_sorted):
            if contact.getName().lower() == name.lower():
                return index
        return -1

    def addContact(self, name: str, fones: list[Fone]):
        contato = self.__find_pos_by_name(name)
        if contato == -1:
            lista = self.getContacts()
            
    def getContacts(self):
        return list(self.__contacts.values())
    
    def rmContact(self, name: str):
        if name in self.__contacts:
            del self.__contacts[name]






    
    
    
    
    

    
        

    

