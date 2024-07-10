def rep_cad():
    print("Bienvenido a el programa 49 con BUCLES REPETIVOS FOR \n")
    print("---------------------------------------------------------")
    print("Repetir una cadena \n")
    print("---------------------------------------------------------")

    cadena = input("Ingresa una cadena de texto: ")

    n = int(input("Ingresa un número entero positivo: "))

    while n <= 0:
        print("Error: Debes introducir un número entero positivo")
        n = int(input("Ingresa un número entero positivo: "))

    for i in range(n):
        print(cadena)    
    input("\n Presiona cualquier tecla para salir del programa: ")
