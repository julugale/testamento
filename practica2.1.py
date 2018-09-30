global indice
indice=5
#se crea una funcion para la pila
class Battery:
   #se incializa un arreglo
   def __init__(self):
      self.items=[] 
   #se crea una funcion para ingresar numeros
   def push(self,item):
      #siempre y cuando el indice lo permita, osea que no este llena
       if len(self.items)<(indice):   
           self.items.append(item)
       else:
           print("innombrable")
           #si esta llena te lo dice
       
pilita = Battery()
print(pilita.pop())
pilita.push("xd")
pilita.push("...")
pilita.push("qwertyuik")
pilita.push("juan")
pilita.push("carlitos")
pilita.push("voldemort")


