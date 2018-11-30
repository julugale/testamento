def naturales(x):
    if x<101:
        print(x)
        x=x+1
        return naturales(x)

def factorialR(num):
    if num==1:
	    return 1
		
    else:
            return num*factorialR(num-1)

def factorialI(num):
    factorial = 1
    while num > 1:
        factorial = factorial * num
        num = num - 1
    return factorial

def fibonacciR(num):
    if num<=1:
	    return 1
		
    else:
            return (fibonacciR(num-1) + fibonacciR(num-2))

def fibonacciI(num):
    a = 1
    b = 0
    for i in range(num):
        a, b = b, a + b
    return b

def Menu():
    print("Menu")
    print("Ingrese numero 1 para Numeros Naturales")
    print("Ingrese numero 2 para Factorial")
    print("Ingrese numero 3 para Fibonacci")
    print("Ingrese numero 4 para salir")
    opc = input()
    if (opc==1):
        print(naturales(1))
        Menu()
        
    if (opc==2):
        print ("Factorial Recursivo")			      
        num=int(input("Ingresa un numero: "))	
        print(factorialR(num))
        print ("----------------------------------------------------------------------")
        print ("Factorial Iterativo")			      
        num=int(input("Ingresa un numero: "))	
        print (factorialI(num))
        Menu()
        
    if (opc==3):
        print ("Fibonacci Recursivo")			      
        num=int(input("Ingresa el limite: "))	
        for i in range(num):
            print (fibonacciR(i))
        print ("----------------------------------------------------------------------")
        print ("Fibonacci Iterativo")			      
        num=int(input("Ingresa el limite: "))	
        for i in range(num+1):
            print (fibonacciI(i))
        Menu()
        
Menu()
