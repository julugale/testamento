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
