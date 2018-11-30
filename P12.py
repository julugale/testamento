
class CC:
   def __init__(self,size):
       self.datos=[]
       self.primero=0
       self.ultimo=-1
       self.size=size
       self.numerodatos=0
       self.aux=0
        
   def colallena(self):
       if self.ultimo==self.size-1:
           return True
       return False    
    
   def colavacia(self):
        if self.numerodatos==0:
            return True
        return False
        
   def push(self,dato):
       if self.colallena()==False:
           self.ultimo+=1
           self.datos.append(dato)
           self.numerodatos+=1
    
   def pop(self):
       if self.colavacia()==False:
           self.aux=self.datos[self.primero]
           self.primero+=1
           self.numerodatos-=1
            

c=CC(5)
c.push(1)
c.push(2)
c.push(3)
c.push(4)
c.push(5)
c.pop()

