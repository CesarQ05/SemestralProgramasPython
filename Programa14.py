def ver_palabra():
    print("Programa 14  Verificar si una palabra tiene más de 5 letras \n")
    # Problema 14 Verificar si una palabra tiene más de 5 letras
    p = input("Bienvenido ingrese una palabra: ")

    if len(p) > 5:
        print(f'Segun la palabra que ingresaste {p} tiene más de 5 letras')
    else:
        print(f'Segun la palabra que ingresaste {p} no tiene más de 5 letras')
        
    input("\n Presiona cualquier tecla para salir del programa: ")
