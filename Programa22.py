def det_asiglo():
    print("Programa 22 Determinar si un año es un siglo \n")
    # Programa 22 Determinar si un año es un siglo
    aio = int(input("Bienvenido ingrese un año: "))


    if aio % 100 == 0:
        print(f'El año {aio} es el primer año de un siglo')
    else:
        print(f'El año {aio} no es el primer año de un siglo')
        
    input("\n Presiona cualquier tecla para salir del programa: ")
