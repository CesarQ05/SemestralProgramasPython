def prog_calificaciones():
    #Programa de promedio de calificaciones
    print("Programa 6 de promedio de calificaciones \n")
    u1 = float(input("Ingrese la primera nota: "))
    u2 = float(input("Ingrese la segunda nota: "))
    u3 = float(input("Ingrese la tercera nota: "))
    u4 = float(input("Ingrese la cuarta nota: "))
    u5 = float(input("Ingrese la quinta nota: "))
    nfinal = (u1 + u2 +u3 + u4 +u5) / 5
    print("El promedio de su nota es:", nfinal)
    
    input("\n Presiona cualquier tecla para salir del programa: ")
