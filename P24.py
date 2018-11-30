class Node(object):
    ##se crea el nodo y los punteros de derecha/izquierda o siguiente/previo 
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next
##variable para imprimir algo
state=False
##se crea la clase de la lista con la cabeza de la lista y la cola de la lista
class DoubleList(object):
    head = None
    tail = None

    ##se agregan elementos a la lista en forma de nodos(solo elemento no siguiente o previo)
    def push(self, data):
        new_node = Node(data, None, None)
        ##se verifica si tiene valor
        if self.head is None:
            self.head = self.tail = new_node
            ##si no, se le da
        else:
            ##se agrega el nodo
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node

    ##se busca el nodo en la lista
    def find(self, node_value):
        q = self.head
        ##se pone el puntero
        global state
        while q is not None:
            ##se verifica si tiene valor
            if q.data == node_value:
                ##si se encuentra se imprime que se encontro
                if q.prev is not None:
                    print("FOUND")
                    state=True

            q = q.next
        ##si no, pues que no se encontro
        if state == True:
                print("NOT FOUND")

    ##si no, pues que no se encontro
    def peek(self):
        print ("LIST:")
        q = self.head
        print(q.data)
        while q is not None:
            ##se imprime
            print(q.next.data) if hasattr(q.next, "data") else None
            q = q.next
        
    def peekreverse(self):
        print ("LIST REVERSE:")
        ##ahora se empieza de la cola parriba
        q = self.tail
        print(q.data)
        while q is not None:
            ##se imprime al reves
            print(q.prev.data) if hasattr(q.prev, "data") else None
            q = q.prev
 
 
d = DoubleList()
d.push("r")

d.push(1)
d.push(2)
d.push(3)
d.push(4)
d.push(5)
d.push(6)
d.push(7)
d.push(8)
d.push(9)

d.peek()
print("******************************************************")
d.push(10)
d.push(11)
d.push(13)
 

print("ROOT")
print(d.head.data)

print("******************************************************")
d.peek()
print("******************************************************")
d.peekreverse()
print("******************************************************")
d.find(0)
d.find(7)
d.find(8)
d.find(1)
