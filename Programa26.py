def lic_conducir():
    print("Programa 26 Determinar el tipo de licencia de conducir \n")
    # Programa 26 Determinar el tipo de licencia de conducir
    edad = int(input("Bienvenido  ingrese su edad: "))

    if 16 <= edad <= 17:
        tipo_licencia = "Licencia de menor"
    elif 18 <= edad <= 65:
        tipo_licencia = "Licencia de adulto"
    elif edad > 65:
        tipo_licencia = "Licencia de adulto mayor"
    else:
        tipo_licencia = "No cumple con la edad mínima para obtener una licencia"


    print(f'Segun su edad {edad} el tipo de licencia de conducir que puede obtener es: {tipo_licencia}')

    input("\n Presiona cualquier tecla para salir del programa: ")
