def fibonacciR(num):
    if num<=1:
	    return 1
		
    else:
            return (fibonacciR(num-1) + fibonacciR(num-2))
print ("Fibonacci Recursivo")			      
num=int(input("Ingresa el limite: "))	
for i in range(num):
	print (fibonacciR(i))

print ("----------------------------------------------------------------------")

def fibonacciI(num):
    a = 1
    b = 0
    for i in range(num):
        a, b = b, a + b
    return b
print ("Fibonacci Iterativo")			      
num=int(input("Ingresa el limite: "))	
for i in range(num+1):
	print (fibonacciI(i))
