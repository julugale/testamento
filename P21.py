class Nodo(): 
	def __init__(self, dato):
		self.dato = dato 
		self.sig = None 
	
		
class Operaciones():
	
	def __init__(self): 
		self.raiz = None 
		self.finT = None 
		self.fin = None 
	
	def Null(self):
		if self.raiz == None: 
			return True
		else:
			return False
		
	def Ingresar(self,dato): 
		
		if self.Null() == True: 
			self.raiz = self.finT = self.fin = Nodo(dato) 
			self.finT.sig = self.fin.sig = self.raiz 
		else:
			temporal = self.fin 
			self.finT = self.fin = temporal.sig = Nodo(dato) 
			self.finT.sig = self.fin.sig = self.raiz 
			
	def Recorrer(self): 
		temp = self.raiz 
		i = True
		if self.Null() == True: 
			print("\n\tNo hay datos registrados...") 
		else:
			while i: 
				print("\t[" + str(temp.dato)+"] ") 
				if temp == self.fin:
					i = False
				else:
					temp = temp.sig 
	
	def Buscar(self,item): 
		self.finT = self.raiz 
		temp = 1 
		
		if self.Null() == True:
			print("\n\tLista vacia")
		else:
			while self.finT.dato != item and temp == 1: 
				if self.finT.sig != self.raiz: 
					self.finT = self.finT.sig 
				else:
					temp = 0
		
			if temp == 0:
				print("\n\tNo existe dato")
			else:
				print("\n\tDato Existente")
				

class  Menu():
	
	def __init__(self): 
		self.opc = None
		
	def capturar(self): 
		captura = Operaciones()
		while True:
			print("\n0.-Guardar datos\n1.-Mostrar datos\n2.-Buscar dato\n6.-Salir")
			self.opc = int(input("\n\tIngrese opcion -> "))
			
			if self.opc == 0:
				x = int(input("\n\tIngresa dato: ")) 
				captura.Ingresar(x)
			
			elif self.opc == 1:
				captura.Recorrer()
			
			elif self.opc == 2:
				date = int(input("\n\tIngresa dato a buscar: "))
				captura.Buscar(date) 
					
			elif self.opc == 6:
				exit()
				
			else: 
				print("\n\tOpcion invalida")


Imprimir = Menu()
Imprimir.capturar()
