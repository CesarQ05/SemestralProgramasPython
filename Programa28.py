def nomb_cortmedia():
    print("Programa 28 Verificar si un nombre es corto, mediano o largo\n")
    #Programa 28 Verificar si un nombre es corto, mediano o largo

    nombre = input("Bienvenido ingrese un nombre: ")

    lon_nombre = len(nombre)


    if lon_nombre < 5:
        categoria = "corto"
    elif 5 <= lon_nombre <= 8:
        categoria = "mediano"
    else:
        categoria = "largo"


    print(f'El nombre {nombre} es de longitud {lon_nombre} y se clasifica como nombre {categoria}')

    input("\n Presiona cualquier tecla para salir del programa: ")
