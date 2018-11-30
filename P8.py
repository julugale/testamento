cola=[]
index=0
size=5
##se crea la cola con valores en 0
def create():
    for u in range(size):
        cola.append(0)
    return cola

##se agregan clientes a la pila almenos que este llena  
def push(Val, index):
    if index < size:
        cola[index] = Val;
    else:
        print("Fila llena, espere afuera de la tienda")

                
##el menu de la cola  
def Menu(index):
    print("Tiendita Chanito")
    print("1 Entrar a la fila")
    print("4 salir")
    o = input()
    if (o=="1" and index <size):
        print("Ingrese el numero que desea ingresar a la pila")
        i = input()
        push(i, index)
        index+=1
        Menu(index)
    if (o=="4"):
        print("bye")
        
create()
Menu(index)   
