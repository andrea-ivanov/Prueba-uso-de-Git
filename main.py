"""
Script básico de ejemplo.
Una pequeña calculadora en consola para practicar
el flujo de trabajo con Git (branch, commit, push, PR).
"""


def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b


def main():
    print("=== Calculadora básica ===")
    print("Operaciones disponibles: +, -, *, /")

    try:
        num1 = float(input("Ingresa el primer número: "))
        operador = input("Ingresa la operación (+, -, *, /): ")
        num2 = float(input("Ingresa el segundo número: "))

        if operador == "+":
            resultado = sumar(num1, num2)
        elif operador == "-":
            resultado = restar(num1, num2)
        elif operador == "*":
            resultado = multiplicar(num1, num2)
        elif operador == "/":
            resultado = dividir(num1, num2)
        else:
            print("Operación no válida.")
            return

        print(f"Resultado: {resultado}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
