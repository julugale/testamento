#se crea una funcion para imprimir los numeros del 1 al 100
def unoalcien(x):
    #se pone un if para que imprima x y si el numero no
    #se pasa de 101 va a seguir sumandole 1 a x, y luego imprimiendolo.
    if x<101:
        print(x)
        x=x+1
        return unoalcien(x)
    #se inicia la funcion
print(unoalcien(1))

