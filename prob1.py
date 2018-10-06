##inciso 1
n=0
##utilizo un if para ir creando los numeros del 1 al 9 y otra variable para irlos sumando
##se usa la misma funcion por lo que es recursiva
def prob1(x,n):
    if x<9:
        x=x+1
        n = n+x
        if n==45:
            print(n)
    return prob1(x,n)
prob1(0,0)

