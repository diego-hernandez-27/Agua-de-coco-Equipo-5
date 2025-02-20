def suma(a, b):
    return a + b

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def __main__():
    print('Hola queridísimo usuario, bienvenido a la calculadora')
    bandera = True

    while bandera:
        print('Elija una opción de la siguiente lista: ')
        print('1. Suma')
        print('2. Resta')
        print('3. Multiplicación')
        print('4. División')
        print('5. Potencia')
        print('6. Factorial')
        print('7. Salir')

        opcion = int(input('Ingrese su opción: '))

        if opcion == 1:
            a = int(input('Ingrese el primer número: '))
            b = int(input('Ingrese el segundo número: '))
            print('Resultado: ' + str(suma(a, b)))
        elif opcion == 6:
            n = int(input('Ingrese un número para calcular su factorial: '))
            if n < 0:
                print('No se puede calcular el factorial de un número negativo.')
            else:
                print(f'El factorial de {n} es: {factorial(n)}')
        elif opcion == 7:
            bandera = False
        else:
            print('Opción no válida')

if __name__ == "__main__":
    __main__()
