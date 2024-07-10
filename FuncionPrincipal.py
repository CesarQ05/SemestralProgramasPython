import Programa1
import Programa2
import Programa3
import Programa4
import Programa5
import Programa6
import Programa7
import Programa8
import Programa9
import Programa10
import Programa11
import Programa12
import Programa13
import Programa14
import Programa15
import Programa16
import Programa17
import Programa18
import Programa19
import Programa20
import Programa21
import Programa22
import Programa23
import Programa24
import Programa25
import Programa26
import Programa27
import Programa28
import Programa29
import Programa30
import Programa31
import Programa32
import Programa33
import Programa34
import Programa35
import Programa36
import Programa37
import Programa38
import Programa39
import Programa40
import Programa41
import Programa42
import Programa43
import Programa44
import Programa45
import Programa46
import Programa47
import Programa48
import Programa49

def main():
    while True:
        print("\n \n 😄=================== Bienvenido a mis programas realizados durnate el semestre===================😄")
        print("\n \n 😄==============================Menú de programas elige una opcion ==========================😄 \n")
        
       
        programas = [
            "1. Suma de 2 números",
            "2. Cálculo del impuesto de un producto",
            "3. Conversión de metros",
            "4. Calcular el volumen de un prisma rectangular",
            "5. Resolución de fórmulas",
            "6. Calcular el promedio de calificaciones",
            "7. Hallar el área de un triángulo rectángulo",
            "8. Hallar perímetro de un rectángulo",
            "9. Hallar el área de un trapecio",
            "10. Verificar si el número es positivo, negativo o cero",
            "11. Determinar si una persona es adolescente",
            "12. Verificar si un número es múltiplo de 5",
            "13. Determinar si un carácter es una vocal",
            "14. Verificar si una palabra tiene más de 5 letras",
            "15. Clasificar la categoría de edad",
            "16. Calcular el precio con descuento",
            "17. Verificar si un número está en un rango",
            "18. Determinar si un carácter es una letra o un dígito",
            "19. Comparar dos números",
            "20. Determinar si un número es primo",
            "21. Calcular el salario neto",
            "22. Determinar si un año es un siglo",
            "23. Verificar si un triángulo es válido",
            "24. Determinar la categoría de un trabajador",
            "25. Clasificar el IMC",
            "26. Determinar el tipo de licencia de conducir",
            "27. Determinar si un número es divisible por 3 y 5",
            "28. Verificar si un nombre es corto, mediano o largo",
            "29. Calcular la tarifa de un taxi",
            "30. Se sumarán los números del 1 al 100",
            "31. Contar hasta un número dado",
            "32. Sumar números hasta un límite",
            "33. Sumar dígitos de un número",
            "34. Adivinar un número",
            "35. Mostrar múltiplos de un número",
            "36. Validar entrada",
            "37. Contador de dígitos de un número",
            "38. Convertir de decimal a binario",
            "39. Simular un cajero automático",
            "40. Tabla de multiplicar",
            "41. Sumar números pares del 1 al 100",
            "42. Contar vocales en una cadena",
            "43. Imprimir una serie de números",
            "44. Imprimir números impares",
            "45. Sumar los primeros N números naturales",
            "46. Determinar si un número es primo",
            "47. Convertir grados Celsius a Fahrenheit",
            "48. Dibujar un triángulo de asteriscos",
            "49. Repetir una cadena"
        ]
        
        # Imprimir el menú en dos columnas
        for i in range(0, len(programas), 2):
            left = programas[i]
            right = programas[i + 1] if i + 1 < len(programas) else ""
            print(f"{left.ljust(60)} {right}")
        
        print("\nq. Salir")
        choice = input("\nElige una opción: ").strip().lower()
        
        # Salir del bucle si la opción es 'q'
        if choice == 'q':
            print("Saliendo...")
            break
        
        
        print("\n")

        
        match choice:
            case "1":
                Programa1.sum_numbers()
            case "2":
                Programa2.cal_impuestos()
            case "3":
                Programa3.conversion_metros()
            case "4":
                Programa4.prisma_rect()
            case "5":
                Programa5.sol_formulas()
            case "6":
                Programa6.prog_calificaciones()
            case "7":
                Programa7.area_triangulo()
            case "8":
                Programa8.p_rectangulo()
            case "9":
                Programa9.a_trap()
            case "10":
                Programa10.ver_num()
            case "11":
                Programa11.p_adolescente()
            case "12":
                Programa12.ver_multiplo()
            case "13":
                Programa13.car_vocal()
            case "14":
                Programa14.ver_palabra()
            case "15":
                Programa15.clasificar_edad()
            case "16":
                Programa16.precio_desc()
            case "17":
                Programa17.ver_numrango()
            case "18":
                Programa18.det_carvocal()
            case "19":
                Programa19.comp_numeros()
            case "20":
                Programa20.det_numprim()
            case "21":
                Programa21.calc_salneto()
            case "22":
                Programa22.det_asiglo()
            case "23":
                Programa23.ver_triangulo()
            case "24":
                Programa24.cat_trabajador()
            case "25":
                Programa25.in_masacop()
            case "26":
                Programa26.lic_conducir()
            case "27":
                Programa27.divisible_tres()
            case "28":
                Programa28.nomb_cortmedia()
            case "29":
                Programa29.calc_tarifataxi()
            case "30":
                Programa30.sum_num()
            case "31":
                Programa31.cont_numdado()
            case "32":
                Programa32.sum_numlim()
            case "33":
                Programa33.sum_entero()
            case "34":
                Programa34.adivinar_num()
            case "35":
                Programa35.multiplio_num()
            case "36":
                Programa36.val_entrada()
            case "37":
                Programa37.cont_dig()
            case "38":
                Programa38.deci_bin()
            case "39":
                Programa39.sim_caj()
            case "40":
                Programa40.tab_mult()
            case "41":
                Programa41.num_imparsum()
            case "42":
                Programa42.contar_vocales()
            case "43":
                Programa43.serie_numeros()
            case "44":
                Programa44.num_impares()
            case "45":
                Programa45.numeros_naturales()
            case "46":
                Programa46.det_numprimo()
            case "47":
                Programa47.grados_cels()
            case "48":
                Programa48.dibujar_triang()
            case "49":
                Programa49.rep_cad()
            case "q":
                print("Saliendo...")
                break
            case _:
                print("Opción no válida, intenta de nuevo.")
                

if __name__ == "__main__":
    main()
