def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multi(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "No se puede dividir por cero"
    return a / b

def potencia(a, b):
    return a ** b

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    print('Hola queridísimo usuario, bienvenido a la calculadora')
    bandera = True

    while bandera:
        print('\nElija una opción de la siguiente lista: ')
        print('1. Suma')
        print('2. Resta')
        print('3. Multiplicación')
        print('4. División')
        print('5. Potencia')
        print('6. Factorial')
        print('7. Salir')

        try:
            opcion = int(input('Ingrese su opción: '))
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")
            continue

        if opcion in [1, 2, 3, 4, 5]:
            try:
                a = float(input('Ingrese el primer número: '))
                b = float(input('Ingrese el segundo número: '))
            except ValueError:
                print("Entrada inválida. Intente nuevamente.")
                continue

            if opcion == 1:
                print('Resultado:', suma(a, b))
            elif opcion == 2:
                print('Resultado:', resta(a, b))
            elif opcion == 3:
                print('Resultado:', multi(a, b))
            elif opcion == 4:
                print('Resultado:', division(a, b))
            elif opcion == 5:
                print('Resultado:', potencia(a, b))

        elif opcion == 6:
            try:
                n = int(input('Ingrese un número para calcular su factorial: '))
                if n < 0:
                    print('No se puede calcular el factorial de un número negativo.')
                else:
                    print(f'El factorial de {n} es: {factorial(n)}')
            except ValueError:
                print("Entrada inválida. Intente nuevamente.")

        elif opcion == 7:
            bandera = False
            print("Gracias por usar la calculadora. ¡Hasta luego!")
        else:
            print('Opción no válida, intente de nuevo.')

if __name__ == "__main__":
    main()
