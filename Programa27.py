def divisible_tres():
    print("Programa 27 Determinar si un número es divisible por 3 y 5 \n")
    # Programa 27 Determinar si un número es divisible por 3 y 5
    numero = int(input("Bienvenido ingresa un número entero: "))

    div_3 = numero % 3 == 0
    div_5 = numero % 5 == 0

    if div_3 and div_5:
        print(f'El numero {numero} es divisible por 3 y por 5')
    elif div_3:
        print(f'El numero {numero} es divisible por 3 pero no por 5')
    elif div_5:
        print(f'El numero {numero} es divisible por 5 pero no por 3"')
    else:
        print(f'El numero {numero} no es divisible ni por 3 ni por 5')

    input("\n Presiona cualquier tecla para salir del programa: ")
