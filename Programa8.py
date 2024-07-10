def p_rectangulo():
    #Programa 8: Hallar perimetro de un rectangulo
    print(" Programa 8 Hallar perimetro de un rectangulo \n")
    nm1 = float(input("Ingrese el lado A: "))
    nm2 = float(input("Ingrese el lado B: "))
    nm3 = float(input("Ingrese el lado C: "))
    nm4 = float(input("Ingrese el lado D: "))
    p = nm1 + nm2 + nm3 + nm4
    print (f'El perimetro del rectangulo con lado A = {nm1}, B = {nm2}, C= {nm3} y D = {nm4} es = {p}')
    
    input("\n Presiona cualquier tecla para salir del programa: ")
