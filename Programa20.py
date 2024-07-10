def det_numprim():
    print("Programa 20 Determinar si un número es primo \n")
    # Programa 20 Determinar si un número es primo
    num = int(input("Bienvenido ingrese un número: "))

    if num <= 1:
        es_primo = False
    else:
        es_primo = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                es_primo = False
                break

    if es_primo:
        print(f"El número {num} es primo")
    else:
        print(f"El número {num} no es primo")
        
    input("\n Presiona cualquier tecla para salir del programa: ")
