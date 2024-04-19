import sys
sys.path.append("src")  # Agrega el directorio "src" al path para importar el módulo personalizado

# Importar las funciones de codificación y decodificación desde el módulo huffman
from huffmanCode.huffman import encode_message, decode_message, encode_message

print("Bienvenido al compresor y descompresor de mensajes!")
print("Seleccione una opción:")
print("1. Comprimir un mensaje")
print("2. Descomprimir un mensaje comprimido")
print("3. Salir")

while True:
    opcion = input("Ingrese el número de su opción: ")

    if opcion == '1':
        message = input("Ingrese el mensaje: ")
        encoded_message, encoding_dict = encode_message(message)
        print("Mensaje codificado:", encoded_message)
        print("Diccionario de codificación:", encoding_dict)
    elif opcion == '2':
        mensaje_comprimido = input("Ingrese el mensaje comprimido a descomprimir: ")
        tree_dict = eval(encoding_dict)
        mensaje_descomprimido = decode_message(mensaje_comprimido, tree_dict)
        print(f"Mensaje descomprimido: {mensaje_descomprimido}")
    elif opcion == '3':
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, intente nuevamente.")