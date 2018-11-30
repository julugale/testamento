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


class  Menu(): 
	def __init__(self): 
		self.opc = None
		
	def capturar(self): 
		captura = Operaciones()  
		while True:  
			print("\n0.-Guardar datos\n6.-Salir")
			self.opc = int(input("\n\tIngrese opcion -> ")) 
			
			if self.opc == 0:
				x = int(input("\n\tIngresa dato: ")) 
				captura.Ingresar(x)
				
			elif self.opc == 6:
				exit() 
				
			else: 
				print("\n\tOpcion invalida")


Imprimir = Menu() 
Imprimir.capturar() 
