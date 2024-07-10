def ver_multiplo():
    # Problema 12: Verificar si un número es múltiplo de 5
    print("Programa 12  Verificar si un número es múltiplo de 5 \n")
    m = int(input("Bienvenido ingrese un número: "))

    #ciclo if para verificar si el numeroe s multiplo de 5
    if m % 5 == 0:
        print(f'Segun el numero que ingresaste {m} es múltiplo de 5')
    else:
        print(f'Segun el numero que ingresaste {m} no es múltiplo de 5')
    
    input("\n Presiona cualquier tecla para salir del programa: ")
    
