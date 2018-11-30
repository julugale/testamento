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
				

	
	def EliminarRaiz(self):
		temp = self.raiz 
		if self.Null() == False:
			self.raiz = self.raiz.sig 
			self.finT.sig = self.fin.sig = self.raiz 
			temp = None 
		else: 
			print("\n\tNo existe raiz para eliminar...")
		
	def Eliminar(self): 
		self.finT = self.raiz 
		temp = self.finT 
		if self.Null() == False:
			if temp != self.fin: 
				while temp.sig != self.fin: 
					temp = temp.sig 
				temp.sig = None 
				self.fin = temp 
				self.finT.sig = self.fin.sig = self.raiz 
			else:
				self.raiz = None 
		else:
		 	print("\n\tNo hay datos para eliminar...")
		 	
	def BuscarEliminar(self,item): 
		self.finT = self.raiz 
		temp = 1 
		
		if self.Null() == True: 
			print("\n\tLista vacia")
		else:
			while self.finT.dato != item and temp == 1: 
				if self.finT.sig != self.raiz:
					self.fin = self.finT   
					self.finT = self.finT.sig 
				else:
					temp = 0
		
			if temp == 0: 
				print("\n\tNo existe el elemento que desea eliminar")
			else:
				if self.raiz == self.finT: 
					self.raiz = self.finT.sig
				else:
					self.fin.sig = self.finT.sig 
				self.finT = None 
				print("\n\tDato eliminado correctamente")

class  Menu(): 
	
	def __init__(self): 
		self.opc = None
		
	def capturar(self):
		captura = Operaciones() 
		while True: 
			print("\n0.-Guardar datos\n1.-Eliminar raiz\n2.-Eliminar Elemento\n3.-Buscar y eliminar\n4.-Mostrar datos\n5.-Buscar dato\n6.-Salir")
			self.opc = int(input("\n\tIngrese opcion -> ")) 
			
			if self.opc == 0:
				x = int(input("\n\tIngresa dato: "))
				captura.Ingresar(x)
			
			elif self.opc == 1:
				captura.EliminarRaiz() 
				
			elif self.opc == 2:
				captura.Eliminar()
			elif self.opc == 3:
				dato = int(input("\n\tIngresa dato a eliminar: "))
				captura.BuscarEliminar(dato) 
				
			elif self.opc == 4:
				captura.Recorrer()	
			
			elif self.opc == 5:
				date = int(input("\n\tIngresa dato a buscar: "))
				captura.Buscar(date) 
					
			elif self.opc == 6:
				exit() 
				
			else:
				print("\n\tOpcion invalida")

Imprimir = Menu()
Imprimir.capturar()
