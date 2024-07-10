def car_vocal():
    # Problema 13 Determinar si un carácter es una vocal
    print("Programa 12  Determinar si un carácter es una vocal \n")
    l = input("Bienvenido ingrese una letra: ")
    # en tal caso de que el ususario ingrese letras en mayusculas se utiliza .lower() para convertirlas en minusculas

    if l in ['a', 'e', 'i', 'o', 'u']:
        print(f'Segun la letra que ingresaste {l} es una vocal')
    else:
        print(f'Segun la letra que ingresaste {l} no es una vocal')
        
    input("\n Presiona cualquier tecla para salir del programa: ")

