def sum_entero():
    print("Bienvenido a el programa 33 con BUCLES REPETIVOS WHILE \n")
    print("---------------------------------------------------------")
    print("Sumar dígitos de un número \n")
    print("---------------------------------------------------------")

    n= int(input("Introduce un número entero: "))

    suma_digitos = 0
    n = abs(n)  

    # Ciclo while para sumar los dígitos del número
    while n > 0:
        digito = n % 10  
        suma_digitos += digito  
        n = n// 10  

    print("La suma de los dígitos es:", suma_digitos)

    input("\n Presiona cualquier tecla para salir del programa: ")
