def grados_cels():
    print("Bienvenido a el programa 47 con BUCLES REPETIVOS FOR \n")
    print("---------------------------------------------------------")
    print("Convertir grados Celsius a Fahrenheit \n")
    print("---------------------------------------------------------")

    i = int(input("Ingresa el inicio del rango en grados Celsius: "))
    f = int(input("Ingresa el fin del rango en grados Celsius: "))

    # Validar que el inicio sea menor o igual al fin
    if i  > f:
        print("Error: El inicio del rango debe ser menor o igual al fin del rango")
    else:
        # Mostrar la tabla de conversión de Celsius a Fahrenheit
        print("Tabla de conversión de Celsius a Fahrenheit:")
        print("Celsius\t\tFahrenheit")
        for celsius in range(i, f + 1):
            fahrenheit = (celsius * 9/5) + 32
            print(f"{celsius}\t\t{fahrenheit:.1f}")

    input("\n Presiona cualquier tecla para salir del programa: ")