def num_impares():
    print("Bienvenido a el programa 44 con BUCLES REPETIVOS FOR \n")
    print("---------------------------------------------------------")
    print("Imprimir números impares \n")
    print("---------------------------------------------------------")

    n = int(input("Ingresa un número entero positivo: "))

    while n <= 0:
        print("Error: Debes introducir un número entero positivo")
        n = int(input("Ingresa un número entero positivo: "))


    print(f"Números impares del 1 al {n}:")
    for num in range(1, n + 1, 2):
        print(num) 
    input("\n Presiona cualquier tecla para salir del programa: ")
