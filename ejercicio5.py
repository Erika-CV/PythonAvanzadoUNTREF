try:
    # Solicitar los números al usuario
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    
    # Intentar realizar la división
    resultado = num1 / num2
    print(f"El resultado de la división es: {resultado}")

except ZeroDivisionError:
    # Capturar la excepción si el segundo número es cero
    print("Error: No se puede dividir entre cero.")

except ValueError:
    # Capturar la excepción si el primer número no es válido
    print("Error: El primer número no es válido. Por favor ingresa un número.")
