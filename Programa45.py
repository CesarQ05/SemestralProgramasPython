def numeros_naturales():
    print("Bienvenido a el programa 45 con BUCLES REPETIVOS FOR \n")
    print("---------------------------------------------------------")
    print("Sumar los primeros N números naturales \n")
    print("---------------------------------------------------------")

    n = int(input("Ingresa un número entero positivo: "))

    while n  <= 0:
        print("Error: Debes introducir un número entero positivo")
        n = int(input("Ingresa un número entero positivo: "))

    suma = 0

    for num in range(1, n  + 1):
        suma += num

    print(f"La suma de los primeros {n } números naturales es: {suma}")

    input("\n Presiona cualquier tecla para salir del programa: ")
