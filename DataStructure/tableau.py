"""
variable = Array(taille,type)
"""
class Array:
    def __init__(self,lenght,_types) -> None:
        self.lenght = lenght
        self.types = _types
        self.array = []
    
    def add(self,element):
        self.array.append(element)

    def delete(self,index):
        del self.array[index]
    def clear(self):
        self.array.clear()
    
        
table = Array(5,int)
table.add(4)
table.add(5)
table.add(6)
table.add(3)
table.remove(2)

print(table.array)

