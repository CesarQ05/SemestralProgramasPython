def comp_numeros():
    print("Programa 19 Comparar dos números \n")
    # Programa 19 Comparar dos números
    n1 = float(input("Bienvenido ingrese el primer número: "))


    n2 = float(input("Bienvenido ingrese el segundo número: "))


    if n1 > n2:
        print(f'El primer número ({n1}) es mayor que el segundo número ({n2})')
    elif n1 < n2:
        print(f'El segundo número ({n2}) es mayor que el primer número ({n1})')
    else:
        print(f'Ambos números son iguales ({n1})')

    input("\n Presiona cualquier tecla para salir del programa: ")
