def in_masacop():
    print("Programa 25 Clasificar el IMC \n")
    # Programa 25 Clasificar el IMC
    peso = float(input("Bienvenido ingrese su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en metros: "))


    imc = peso / (altura ** 2)

    if imc < 18.5:
        categoria = "Bajo peso"
    elif 18.5 <= imc < 24.9:
        categoria = "Normal"
    elif 25 <= imc < 29.9:
        categoria = "Sobrepeso"
    else:
        categoria = "Obesidad"

    print(f'Segun Su IMC: {imc}, usted esta en {categoria}')
    
    input("\n Presiona cualquier tecla para salir del programa: ")
