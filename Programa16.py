def precio_desc():
    # Programa 16 Calcular el precio con descuento
    print("Programa 16 Calcular el precio con descuento \n")
    pre = float(input("Bienvenido ingrese el precio del producto: "))

    #utilizamos el if si el precio es mayor a $100 y aplicar el descuento si corresponde
    if pre > 100:
        des = pre * 0.10
        p_final = pre - des
        print(f'El precio final después de aplicar un descuento del 10% es: ${p_final}')
    else:
        pr_final = pre
        print(f'El precio final es: ${pr_final}')
        
    input("\n Presiona cualquier tecla para salir del programa: ")
