def num_imparsum():
    print("Bienvenido a el programa 41 con BUCLES REPETIVOS FOR \n")
    print("---------------------------------------------------------")
    print("Sumar números pares del 1 al 100 \n")
    print("---------------------------------------------------------")

    suma_pares = 0

    for num in range(2, 101, 2):
        suma_pares += num


    print(f"La suma de los números pares del 1 al 100 es: {suma_pares}")

    input("\n Presiona cualquier tecla para salir del programa: ")
