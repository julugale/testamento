global indice
indice=5
#se crea una funcion para la pila
class Battery:
      #se incializa un arreglo
   def __init__(self):
      self.items=[]
      #se checa si esta vacio el arreglo
   def taVacia(self):
      return (self.items) == []    
      #se mete el valor en la parte de arriba de la pila si no esta llena
   def push(self,item):
       if len(self.items)<(indice):   
           self.items.append(item)
       else:
           #si esta llena te lo dice
           print("pila llena")
      #se saca el valor de arriba de la pila si no esta vacia
   def pop(self):
        if 0 < len(self.items):
           print("popeado:")
           print(self.items[len(self.items)-1])
           del(self.items[len(self.items)-1])
        else:
           #si esta vacio te lo dice
           print("vacio")
      #checa el tamanno de la pila
   def size(self):
       return len(self.items)
      #checa el valor de arriba de la pila
   def peek(self):
       return self.items[-1]
       
       
pilita = Battery()
pilita.pop()
pilita.push("xd")
pilita.push("...")
pilita.push("qwertyuik")
pilita.push("juan")
pilita.push("carlitos")
pilita.push("voldemort")
pilita.pop()
