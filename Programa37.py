def cont_dig():
    print("Bienvenido a el programa 37 con BUCLES REPETIVOS WHILE \n")
    print("---------------------------------------------------------")
    print("Contador de dígitos \n")
    print("---------------------------------------------------------")

    num = int(input("Introduce un número entero: "))

    0
    if num == 0:
        print("El número 0 tiene 1 dígito")
    else:
        contador_digitos = 0
        num = abs(num)

        while num > 0:
            num = num// 10  
            contador_digitos += 1  

        print(f"El número tiene {contador_digitos} dígitos")


    input("\n Presiona cualquier tecla para salir del programa: ")
