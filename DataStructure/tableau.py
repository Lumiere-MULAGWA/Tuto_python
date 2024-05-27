"""
variable = Array(taille,type)
"""
class Array:
    def __init__(self,lenght,_types) -> None:
        self.lenght = lenght
        self.types = _types
        self.array = []
    
    def add(self,*element):
        self.array.append(element)

    def remove(self,element):
        del self.array(element)
        
table = Array(5,int)
table.add(4,5,6,7)
table.remove(2)
print(table.array)

