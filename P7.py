class Battery:
   ##se crea la pila
   def __init__(self):
      self.items=[]
      size = 5
      
   ##se ingresan versiones a la pila
   def push(self,item):
       if len(self.items)<(indice):   
           self.items.append(item)
       else:
      ##al menos que este llena
           print("Lista llena")
           
   ##se crea la pila
   def pop(self):
       if len(self.items)>(0):
           self.items.pop()
       else:
          ##al menos que este vacia
          print("Lista vacia")
   ##se imprimen las versiones    
   def peek(self):
    print("Consultar versiones")
    print("1 Consultar ultima version agregada")
    print("2 Consultar todas las versiones")
    print("3 Buscar una version")
    p = input();
    if(p=="1"):
        if 0 < len(pila):
            print("Ultima Version:")  
            print(self.items[len(self.items)-1])
            print("Indice:")
            print(len(self.items)-1)
            print("Valor agregado")
        else:
            print("Lista Vacia");
    if(p=="2"):
        if 0 < len(self.items):
            print("Todas las Versiones")
            for Num in reversed(self.items):
                print(Num)
    if(p=="3"):
        if 0 < len(self.items):
            print("Ingresar Version:")
            i = input()
            for Num in self.items:
                if (Num==i):
                    print("Version encontrada")
                    print(self.items.index(Num))
                    
                    Menu();
            
            print("Version no encontrada")
        else:
            print("Lista Vacia")
   ##el menu de opciones
   def Menu(self):
    print("Control de Versiones")
    print("1 Agregar version a la lista")
    print("2 Eliminar ultima version")
    print("3 Consultar versiones")
    print("4 Salir")
    o = input()
    if (o=="1"):
        print("Ingresar numero de version")
        n = input()
        pil.push(n)
        pil.Menu()
        
    if (o=="2"):
        pil.pop()
        pil.Menu()
    if (o=="3"):
        pil.peek()
        pil.Menu()

pil = Battery()
pil.Menu()
