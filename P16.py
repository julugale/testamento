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
			
	def PopRear(self): 
		if self.Front != self.Rear:
			self.Rear += 1 
			self.datos[self.Rear] = 0 
			aux = self.datos[self.Rear-1] 
		else:
			print("NO DATA")
	
	def PopFront(self):
		if self.Front != self.Rear: 
			self.Front -= 1 
			self.datos[self.Front] = 0 
			aux = self.datos[self.Front+1] 
		else:
			print("NO DATA")
			
	def  peekall(self): 
		print("")
		for i,j in enumerate(self.datos): 
			print('\t\t\t'+str([i,j]))
			
	def peekfirst(self): 
		if self.Front != 0:
			print("Front [" + str(self.datos[self.Front]) + "]")
		else: 
			print("No hay dato proximo a salir, ingresa datos")	
			
	def Peeklast(self): 
		if self.Rear != 0:
			print("Rear [" + str(self.datos[self.Rear]) + "]")
		else: 
			print("Registre datos; Cola vacia")	
	
	def peekindex(self,item): 
		z=-1 
		for i in range(0,len(self.datos)): 
			if self.datos[i] == item: 
				z=i 
		return z
	
	def Menu(self): 
		while True: 
                        print("1 Push Rear")
                        print("2 Push Front")
                        print("3 Pop Rear")
                        print("4 Pop Front")
                        print("5 Peek All")
                        print("6 Peek Front")
                        print("7 Peek Rear")
                        print("8 peek Index")
                        print("9 Salir")
			o = int(input())
			if o == 1:
				x=int(input("Ingresa dato ")) 
				print("")
				self.pushRear(x)
			elif o == 2:
				x=int(input("Ingresa dato "))
				print("")
				self.pushFront(x)
			elif opc == 3:
				self.PopRear() 
			elif opc == 4:
				self.PopFront() 
			elif opc == 5:
				self.peekall()
			elif opc == 6:
				self.peekfirst()
			elif opc == 7:
				self.Peeklast()
			elif opc == 8:
				dato= int(input("Ingresa dato a buscar "))
				p = self.peekindex(dato) 
				if p != -1: 
					print('Dato [' + str(dato) +'] En posicion [' + str(p) + ']')
				else:
					print("No encontrado")
								
			elif o==9:
				exit()			
			else : 
				print("?")
			

up = Bass()
up.Menu()
