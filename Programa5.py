def sol_formulas():
    # Algoritmo de resolucion de formulas
    print("Programa  5 de resolucion de formulas \n")
    a = float(input("Ingrese 'a' para la operacion: "))
    b = float(input("Ingrese 'b' para la operacion: "))
    c = float(input("Ingrese 'c' para la operacion: "))
    o1 = (4 * a) + (3 * b)
    o2 = (21 * a) - 18 + (8 * b) - 5
    o3 = (4 * a) + (3 * b) + 7
    o4 = (2 * a) + (3 * b) - (c ** 5)
    o5 = (2 * a) + (3 * b) - (c ** 2)
    print (f'Los valores proporcionados para hacer las operaciones son a = {a}, b = {b}, c = {c}')
    print (f'El resultado operacion 1 (4a + 3b) es = {o1}')
    print (f'El resultado operacion 2 (21a - 18 + 18b - 5) es = {o2}')
    print (f'El resultado operacion 3 (4a + 3b + 7) es = {o3}')
    print (f'El resultado operacion 4 (2a + 3b - c^5) es = {o4}')
    print (f'El resultado operacion 5 (2a + 3b - c^2) es = {o5}')
    
    input("\n Presiona cualquier tecla para salir del programa: ")
