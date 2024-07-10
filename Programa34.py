def adivinar_num():
    print("Bienvenido a el programa 34 con BUCLES REPETIVOS WHILE \n")
    print("---------------------------------------------------------")
    print("Adivinar un número \n")
    print("---------------------------------------------------------")

    import random


    numero_aleatorio = random.randint(1, 10)

    print("Adivina el número entre 1 y 10")

    adivinanza = 0
    while adivinanza != numero_aleatorio:
        adivinanza = int(input("Introduce tu adivinanza: "))

        if adivinanza < numero_aleatorio:
            print("El número es mayor")
        elif adivinanza > numero_aleatorio:
            print("El número es menor")
        else:
            print("¡Felicidades! Has adivinado el número")
            
    input("\n Presiona cualquier tecla para salir del programa: ")
