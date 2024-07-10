def det_carvocal():
    print("Programa 18 Determinar si un carácter es una letra o un dígito \n")
    # Programa 18 Determinar si un carácter es una letra o un dígito
    c = input("Bienvenido ingrese un carácter: ")


    if ('a' <= c <= 'z') or ('A' <= c <= 'Z'):
        print(f'Segun el caracter que ingresaste {c} es una letra')
    elif '0' <= c <= '9':
        print(f'Segun el caracter que ingresaste {c} es un digito')
    else:
        print(f'Segun el caracter que ingresaste {c} no es una letra ni un digito')
    
    input("\n Presiona cualquier tecla para salir del programa: ")
