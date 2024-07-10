def sum_numlim():
    print("Bienvenido a el programa 32 con BUCLES REPETIVOS WHILE \n")
    print("---------------------------------------------------------")
    print("Sumar números hasta un límite \n")
    print("---------------------------------------------------------")


    limite = 10


    suma = 0


    while suma < limite:
        numero = int(input("Introduce un número entero: "))
        if numero > 0:
            suma += numero
            print(f"Suma actual: {suma}")
        else:
            print("Por favor, introduce otro número entero")

    print("Se ha alcanzado el límite de suma.")


    input("\n Presiona cualquier tecla para salir del programa: ")
