def Menu():
    print("Menu")
    print("1 Practica 1")
    print("2 Practica 2")
    print("3 Practica 3")
    print("4 Salir")
    o = input();
    if(o=="1"):
        #Prac 1
        print("42783")
        def unoalcien(x):
            if x<101:
                print(x)
                x=x+1
                return unoalcien(x)
        print(unoalcien(1))
        Menu()
        
    if(o=="2"):
        #Prac 2
        num = int(input("Ingresa un numero: "))
        factorial = 1
        for i in range(num):
            print (factorial, " * " , num)
            factorial = factorial * num
            num = num - 1 
        print (factorial)
        Menu()
        
    if(o=="3"):
        #Prac 3
        n = int(input("Ingresa un numero: "))
        n=n+1
        def fibonacho(n):
            if n <= 1:
                return n
            else:
               return(fibonacho(n-1) + fibonacho(n-2))
        if n <= 0:
           print("no es positivo beep boop")
        else:
           print("Fibonacho: ")
           for i in range(n):
               print(fibonacho(i))
        Menu()

Menu()
