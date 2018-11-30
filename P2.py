def factorialR(num):
    if num==1:
	    return 1
		
    else:
            return num*factorialR(num-1)
print ("Factorial Recursivo")			      
num=int(input("Ingresa un numero: "))	
print(factorialR(num))

print ("----------------------------------------------------------------------")


def factorialI(num):
    factorial = 1
    while num > 1:
        factorial = factorial * num
        num = num - 1
    return factorial

print ("Factorial Iterativo")			      
num=int(input("Ingresa un numero: "))	
print (factorialI(num))
