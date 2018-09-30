#funcion para factorial de un numero ingresado por ususario
#se pide el numero al usuario
num = int(input("Ingresa un numero: "))
#se inicializa el factorial en 1
factorial = 1
#se crea un ciclo para que se multiplique el numero de vecews dada por el usuario
for i in range(num):
    print (factorial, " * " , num)
    factorial = factorial * num
    num = num - 1 
#se imprime
print (factorial)
    
    
