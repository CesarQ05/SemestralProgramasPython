def sim_caj():
    print("Bienvenido a el programa 39 con BUCLES REPETIVOS WHILE \n")
    print("---------------------------------------------------------")
    print("Simular un cajero automático \n")
    print("---------------------------------------------------------")

    pin_correcto = "1234"
    intentos = 3

    while intentos > 0:
        pin_usuario = input("Bienvenidos porfavor ingresa tu PIN: ")

        if pin_usuario == pin_correcto:
            print("PIN correcto, acceso concedido")
            #break
        else:
            intentos -= 1  
            if intentos > 0:
                print(f"PIN incorrecto. Te quedan {intentos} intentos")
            else:
                print("¡Has agotado tus intentos! Tarjeta bloqueada")



    input("\n Presiona cualquier tecla para salir del programa: ")
