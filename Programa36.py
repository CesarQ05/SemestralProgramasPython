def val_entrada():
    print("Bienvenido a el programa 36 con BUCLES REPETIVOS WHILE \n")
    print("---------------------------------------------------------")
    print("Validar entrada \n")
    print("---------------------------------------------------------")


    n = int(input("Ingresa un número positivo: "))


    while n <= 0:
        print("Error: Debes ingresar un número positivo.")
        n = int(input("Ingresa un número positivo: "))

    print("Has ingresado un número positivo:", n)


    input("\n Presiona cualquier tecla para salir del programa: ")
