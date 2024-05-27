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
        try:
            del self.array[index]
        except:
            print("imposibe de delete")
    def remove(self,element):
        try:
            self.array.remove(element)
        except:
            print("impossible de remove ")
    def clear(self):
        self.array.clear()
    
        
table = Array(5,int)
table.add(4)
table.add(5)
table.add(6)
table.add(3)
table.delete(10)

print(table.array)

