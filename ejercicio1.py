try:
    # Solicitar los números al usuario
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    
    # Intentar dividir los números
    resultado = num1 / num2
    print(f"El resultado de la división es: {resultado}")
    
except ZeroDivisionError:
    # Capturar la excepción si el segundo número es cero
    print("Error: No se puede dividir entre cero.")
except ValueError:
    # Capturar el caso en que no se ingrese un número válido
    print("Error: Por favor ingresa valores numéricos válidos.")
