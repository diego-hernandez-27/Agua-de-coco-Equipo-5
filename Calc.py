
def division(a,b):
    if(b==0):
        return "No se puede dividir por cero"
    return a/b
    

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b
  
def multi(a,b):
	return a * b

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
        elif opcion == 4:
            a = int(input('Ingrese el primer número: '))
            b = int(input('Ingrese el segundo número: '))
            print('Resultado: ' + str(division(a,b)))
        elif opcion == 2:
            a = int(input('Ingrese el primer número: '))
            b = int(input('Ingrese el segundo número: '))
            print('Resultado: ' + str(resta(a, b)))
        elif opcion == 3:
            a = int(input('Ingrese el primer número: '))
            b = int(input('Ingrese el segundo número: '))
            print('Resultado: ' + str(multi(a, b)))
        elif opcion == 7:
            bandera = False
        else:
            print('Opción no válida')

if __name__ == "__main__":
    __main__()
