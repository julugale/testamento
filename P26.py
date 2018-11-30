class Nodo(object):
	
	def __init__(self, dato):
		self.dato = dato
		self.izquierda = None
		self.derecha = None
	
	def __str__(self):
		return '%s' % (self.dato) 
	
class Arbol(object):
	
	def __init__(self):
		self.root = None
	
	def agregar(self,dato):
		if self.root == None:
			self.root = Nodo(dato)
		else:
			aux = self.root
			padre = None
			while aux != None:
				padre = aux
				if dato >= aux.dato:
					aux = aux.derecha
				else:
					aux = aux.izquierda
					
			if dato >= padre.dato:
				padre.derecha = Nodo(dato)
			else:
				padre.izquierda = Nodo(dato)
