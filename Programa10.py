def ver_num():
    # Problema 10 con Sentencia selectivas IF
    print("Programa 10  Verificar si el numero es positivo, negativo o cero \n")
    n = float(input("Bienvenido ingrese un número: "))

    #ciclo if para verificar si el numero es positivo, negativo o cero. 
    if n > 0:
        print(f'El número es que ingresaste {n} es positivo')
    elif n < 0:
        print(f'El número es que ingresaste {n} es negativo')
    else:
        print(f'El número es que ingresaste {n} es cero')
    
    input("\n Presiona cualquier tecla para salir del programa: ")
