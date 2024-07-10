def a_trap():
    #Programa 9 Hallar el area de un trapecio
    print("Programa 9 Hallar el area de un trapecio \n")
    nin1 = float(input("Ingrese la base 1 del trapecio: "))
    nin2 = float(input("Ingrese la base 2 del trapecio: "))
    nin3 = float(input("Ingrese la altura del trapecio: "))
    a = ((nin1 + nin2) * nin3) / 2
    print (f'El area del trapecio con base 1= {nin1}, base 2= {nin2} y altura {nin3} es = {a}')
    
    input("\n Presiona cualquier tecla para salir del programa: ")
