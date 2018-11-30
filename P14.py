class Bass(object):
	def __init__(self):
		self.datos =   [0,0,0,0,0,0,0,0,0,0]
		self.Front = 0 
		self.Rear = 0 

	def pushFront(self,item):
		if self.Front == 5: 
			print("Limite de 5")
		else:
			self.Front += 1 
			self.datos[self.Front] = item 
	
	def pushRear(self,item): 
		if self.Rear == -5:  
			print("Limite de 5")
		else:
			self.Rear -= 1 
			self.datos[self.Rear] = item 

	def Menu(self): 
		while True:
                        print("1 Push Rear")
                        print("2 Push Front")
                        print("4 Salir")
			o = int(input())
			if o == 1:
				x=int(input("Ingresa dato")) 
				print("")
				self.pushRear(x)
			elif o == 2:
				x=int(input("Ingresa dato"))
				print("")
				self.pushFront(x)
			elif o==9:
				exit()			
			else : 
				print("?")
				
up = Bass()
up.Menu()
