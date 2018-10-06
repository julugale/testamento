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

##se despachan clinetes al menos que no haya clientes  
def pop(index):
    if index>0:
        print("Cliente despachado:")
        print(cola[0])
        ind=0
        for I in range(size-1):
            cola[ind]=cola[ind+1]
            ind+=1
        cola[index-1]=0  
    else:
        print("Fila vacia, no hay cliente por despachar")

##se imprime la lista de personas haciendo fila  
def peek():
        if 0 < len(cola):
            print("Los clientes en espera son estos")
            for Num in cola:
                print(Num)
                
##el menu de la cola  
def Menu(index):
    print("Tiendita Chanito")
    print("1 Entrar a la fila")
    print("2 Salir de la fila")
    print("3 Checar la fila")
    print("4 salir")
    o = input()
    if (o=="1" and index <size):
        print("Ingrese el numero que desea ingresar a la pila")
        i = input()
        push(i, index)
        index+=1
        Menu(index)
    if (o=="2" and index > 0):
        pop(index)
        index-=1
        Menu(index)
    if (o=="3"):
        peek()
        Menu(index)    
create()
Menu(index)   



