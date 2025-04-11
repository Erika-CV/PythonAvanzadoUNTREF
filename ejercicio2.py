try:
    # Solicitar los datos al usuario
    num = float(input("Ingresa un número: "))
    cadena = input("Ingresa una cadena de texto: ")
    
    # Intentar sumar el número y la cadena
    resultado = num + cadena
    print(f"El resultado de la suma es: {resultado}")
    
except TypeError:
    # Capturar la excepción si ocurre un error de tipo
    print("Error: No se puede sumar un número y una cadena.")
except ValueError:
    # Capturar el caso en que no se ingrese un número válido
    print("Error: Por favor ingresa un valor numérico válido para el número.")
