def cal_impuestos():
    # Programa 2: Calculo del impuesto de un producto
    print("Programa 2 Calculo del impuesto de un producto \n")
    num1 = float(input("Ingrese el precio del producto: "))
    num2 = int(input("Ingrese la cantidad que vas a comprar: "))
    num3 = float(input("Ingrese el impuesto que tiene el producto: "))
    pc= num1 * num2
    pi = pc * num3
    imp= pc + pi
    print (f'El impuesto del producto que pagas es {num3}, mas el precio que vale {num1}, lo que tienes que pagar es: {pc}')
    print (f'El precio de la compra total {num1} por la cantidad {num2} con impuesto incluido es {imp}')
    
    input("\n Presiona cualquier tecla para salir del programa: ")
