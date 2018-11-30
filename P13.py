class CC:
   def __init__(self,size):
       self.datos=[]
       self.front=0
       self.rear=0
       self.size=size
       self.index=0
       for I in range(size):
            self.datos.append(0)
        
        
   def push(self,dato):
       if self.datos[self.front]==0:
           self.rear+=1
           self.datos.append(self.front)
           self.index+=1
    
   def pop(self):
       if self.datos[self.front]==0:
           self.front+=1
           self.index-=1
      
   def verfront(self):
       print(self.datos[self.front])
        
   def verrear(self):
       print(self.datos[self.rear])        
        
        
   def visualize(self):
       for i in range(self.front,self.rear):
           print(self.datos[i])

c=CC(5)
c.push(1)
c.push(2)
c.push(3)
c.push(4)
c.push(5)
c.verfront()
c.verrear()
c.visualize()
c.pop()
c.visualize

