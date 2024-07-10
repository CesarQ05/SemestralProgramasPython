def sum_num():
    print("Bienvenido a el programa 30 con BUCLES REPETIVOS WHILE \n")
    print("---------------------------------------------------------")
    print("Se sumaran los números del 1 al 100 \n")
    print("---------------------------------------------------------")

    suma = 0
    num = 1


    while num<= 100:
        suma += num
        num += 1
        
        print ("Suma:", suma)
        print ("Numero:", num)

    print("La suma de los números del 1 al 100 es:", suma)

    input("\n Presiona cualquier tecla para salir del programa: ")
