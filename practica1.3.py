#se pide un numero
n = int(input("Ingresa un numero: "))
#se agrega uno aqui por que n empieza en 0 y ocupo que empieze en 1
n=n+1
#se crea una funcion de fibonachi recursiva
def fibonacho(n):
    if n <= 1:
        return n
    else:
       return(fibonacho(n-1) + fibonacho(n-2))
#se pone la limitacion de mayor a 0    
if n <= 0:
   print("no es positivo beep boop")
else:
   print("Fibonacho: ")
   #ciclo para imprimir todos los numeros fibonachis hasta el numero dado
   for i in range(n):
       print(fibonacho(i))
    
    
