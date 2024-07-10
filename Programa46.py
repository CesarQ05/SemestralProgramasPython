def det_numprimo():
    print("Bienvenido a el programa 46 con BUCLES REPETIVOS FOR \n")
    print("---------------------------------------------------------")
    print("Determinar si un número es primo \n")
    print("---------------------------------------------------------")

    numero = int(input("Ingresa un número entero positivo: "))

    while numero <= 0:
        print("Error: Debes introducir un número entero positivo")
        numero = int(input("Ingresa un número entero positivo: "))

    es_primo = True
    if numero == 1:
        es_primo = False
    elif numero == 2:
        es_primo = True
    elif numero % 2 == 0:
        es_primo = False
    else:
        for i in range(3, int(numero**0.5) + 1, 2):
            if numero % i == 0:
                es_primo = False
                break
    if es_primo:
        print(f"{numero} es un número primo")
    else:
        print(f"{numero} no es un número primo")
      
    input("\n Presiona cualquier tecla para salir del programa: ")
