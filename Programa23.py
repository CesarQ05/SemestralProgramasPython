def ver_triangulo():
    print("Programa 23 Verificar si un triángulo es válido \n")
    #Programa 23 Verificar si un triángulo es válido
    l1 = float(input("Bienvenido ingrese la longitud del primer lado: "))
    l2 = float(input("Bienvenido ingrese la longitud del segundo lado: "))
    l3 = float(input("Bienvenido ingrese la longitud del tercer lado: "))

    # Verificar si se cumple la desigualdad triangular
    if (l1 + l2 > l3) and (l1 + l3 > l2) and (l2 + l3 > l1):
        print(f'Las longitudes ingresadas {l1}, {l2}, {l2} forman un triángulo válido')
    else:
        print(f'Las longitudes ingresadas {l1}, {l2}, {l2} no forman un triángulo válido')
        input("\n Presiona cualquier tecla para salir del programa: ")
    
    input("\n Presiona cualquier tecla para salir del programa: ")
