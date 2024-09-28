# main.py

from calculator.calculator import Calculator

def main():
    calc = Calculator()
    while True:
        print("\nSeleccione una operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
        choice = input("Ingrese una opción (1-5): ")

        if choice == '5':
            print("Saliendo de la calculadora.")
            break

        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if choice == '1':
            result = calc.add(num1, num2)
            operation = 'Suma'
        elif choice == '2':
            result = calc.subtract(num1, num2)
            operation = 'Resta'
        elif choice == '3':
            result = calc.multiply(num1, num2)
            operation = 'Multiplicación'
        elif choice == '4':
            result = calc.divide(num1, num2)
            operation = 'División'
        else:
            print("Opción inválida.")
            continue

        print(f"El resultado de la {operation} es: {result}")
        calc.logger.log_operation(operation, num1, num2, result)

if __name__ == "__main__":
    main()