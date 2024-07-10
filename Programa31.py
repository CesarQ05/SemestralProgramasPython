def cont_numdado():
    print("Bienvenido a el programa 31 con BUCLES REPETIVOS WHILE \n")
    print("---------------------------------------------------------")
    print("Contar hasta un número dado \n")
    print("---------------------------------------------------------")


    n = int(input("Introduce un número entero positivo: "))


    contador = 1


    while contador <= n:
        print(contador)
        contador += 1

    input("\n Presiona cualquier tecla para salir del programa: ")
