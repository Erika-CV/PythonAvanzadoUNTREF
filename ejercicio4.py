try:
    # Intentar abrir un archivo que no existe
    nombre_archivo = input("Ingresa el nombre del archivo a abrir: ")
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read()
        print("Contenido del archivo:")
        print(contenido)

except FileNotFoundError:
    # Si el archivo no existe, captura la excepción y muestra el mensaje
    print(f"Error: El archivo '{nombre_archivo}' no se encuentra.")
    # Intentar crear el archivo si no existe
    with open(nombre_archivo, 'w') as archivo:
        archivo.write("Este es un archivo nuevo creado porque no existía.")
    print(f"El archivo '{nombre_archivo}' ha sido creado exitosamente.")
