print ("Bienvenido a la calculadora. ¿Qué operación desea realizar?")

import math

while True:
    print("--- CALCULADORA ---")
    print("1) Suma")
    print("2) Resta")
    print("3) Multiplicación")
    print("4) División")
    print("5) Raiz cuadrada")
    print("6) Potencia")
    print("7) Seno")
    print("8) Salir")

    opcion = int(input("Seleccione una opción: "))
    if opcion == 8:
        print("Gracias por utilizar la calculadora.")
        break

    num1 = int(input("Ingrese el primer número: "))
    if opcion not in [5,6,7]:
        num2 = int(input("Ingrese el segundo número: "))
    if opcion == 1:
        resultado = num1 + num2
        print("El resultado es:", resultado)
    elif opcion == 2:
        resultado = num1 - num2
        print("El resultado es:", resultado)
    elif opcion == 3:
        resultado = num1 * num2
        print("El resultado es:", resultado)
    elif opcion == 4:
        if num2 != 0:
            resultado = num1 / num2
            print("El resultado es:", resultado)
        else:
            print("División por cero no permitida.")
    elif opcion == 5:
        resultado = math.sqrt(num1)
        print("La raiz cuadrada de ",num1, "es: ",resultado)
    elif opcion == 6:
        exponente = int(input("Ingrese el exponente: "))
        resultado = math.pow(num1, exponente)
        print(num1, "elevado a la potencia", exponente, "es: ",resultado)
    elif opcion == 7:
        resultado = math.sin(num1)
        print("El seno de", num1, "es: ",resultado)

    
