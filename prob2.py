##inciso 2
def potencia(n):
    ##se verifica que no sea menor a 0
    if n <= 0:
        return 1
    ##determinar si la potencia es par o impar
    if n % 2 == 0:
        pot = potencia(n/2)
        return pot * pot
    else:
        pot = potencia((n-1)/2)
        return pot * pot * 2
print(potencia(5))
