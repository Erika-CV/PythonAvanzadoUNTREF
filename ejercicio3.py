# Definir un diccionario con algunas claves y valores
diccionario = {'nombre': 'Juan', 'edad': 25, 'ciudad': 'Madrid'}

try:
    # Intentar acceder a una clave que no existe
    clave = input("Ingresa la clave que deseas buscar: ")
    valor = diccionario[clave]  # Intentamos acceder a la clave
    print(f"El valor de la clave '{clave}' es: {valor}")

except KeyError:
    # Capturar la excepción si la clave no existe en el diccionario
    print(f"Error: La clave '{clave}' no existe en el diccionario.")
