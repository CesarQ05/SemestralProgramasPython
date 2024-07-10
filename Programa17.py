def ver_numrango():
    print("Programa 17 Verificar si un número está en un rango \n")
    #Programa 17 Verificar si un número está en un rango

    nn = int(input("Bienvenido ingrese un número: "))

    # Verificar si el número está entre 1 y 100 inclusive
    if 1 <= nn <= 100:
        print(f'Segun el numero que ingresaste {nn} está entre 1 y 100 inclusive')
    else:
        print(f'Segun el numero que ingresaste {nn} no está entre 1 y 100 inclusive')
        
    input("\n Presiona cualquier tecla para salir del programa: ")
