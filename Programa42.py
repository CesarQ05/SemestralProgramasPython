def contar_vocales():
    print("Bienvenido a el programa 42 con BUCLES REPETIVOS FOR \n")
    print("---------------------------------------------------------")
    print("Contar vocales en una cadena \n")
    print("---------------------------------------------------------")


    c = input("Ingresa una cadena de texto: ")

    # Definir las vocales
    vocales = "aeiouAEIOU"

    # Inicializar el contador de vocales
    contador_vocales = 0

    # Ciclo for para contar las vocales en la cadena
    for caracter in c:
        if caracter in vocales:
            contador_vocales += 1

    # Mostrar el resultado
    print(f"El número de vocales que hay en la cadena {c} es: {contador_vocales}")

        
    input("\n Presiona cualquier tecla para salir del programa: ")
