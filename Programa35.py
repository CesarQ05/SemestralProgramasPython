def multiplio_num():
    print("Bienvenido a el programa 35 con BUCLES REPETIVOS WHILE \n")
    print("---------------------------------------------------------")
    print("Mostrar múltiplos de un número \n")
    print("---------------------------------------------------------")

    n = int(input("Introduce un número entero positivo: "))


    while n <= 0:
        print("Error: Debes introducir un número entero positivo.")
        n = int(input("Introduce un número entero positivo: "))


    contador = 1

    while contador <= 10:
        multiplo = n * contador
        print(f"{n} x {contador} = {multiplo}")
        contador += 1

    input("\n Presiona cualquier tecla para salir del programa: ")
