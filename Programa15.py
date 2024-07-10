def clasificar_edad():
    # Problema 15 Clasificar la categoría de edad
    print("Programa 15 Clasificar la categoría de edad \n")
    ed = int(input("Bienvenido ingrese su edad: "))


    if 0 <= ed  <= 12:
        print(f'Segun la edad que ingresaste {ed} usted es infantil')
    elif 13 <= ed  <= 19:
        print(f'Segun la edad que ingresaste {ed} usted es Adolescente')
    elif 20 <= ed  <= 59:
        print(f'Segun la edad que ingresaste {ed} usted es Adulto')
    elif ed  >= 60:
        print(f'Segun la edad que ingresaste {ed} usted es Adulto mayor')
    else:
        print(f'La edad que ingresaste {ed} no es válida')
        
    input("\n Presiona cualquier tecla para salir del programa: ")
