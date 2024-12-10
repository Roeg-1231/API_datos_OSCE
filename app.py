import json

# Leer el archivo original (en este caso, el contenido es una cadena de texto).
with open('adjudicaciones.json', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Crear una nueva lista de líneas modificadas con el formato correcto
formatted_lines = []
for line in lines:
    # Agregar el espacio después de cada ":"
    formatted_line = line.replace(':', ': ')
    formatted_lines.append(formatted_line)

# Asegurarse de que hay una coma después de cada cierre de llave, excepto la última entrada
json_content = ''.join(formatted_lines)

# Buscamos todas las llaves de cierre y les agregamos la coma cuando corresponda
json_content = json_content.replace('}\n{', '},\n{')

# Escribir el archivo modificado
with open('adjudicaciones_v2.json', 'w', encoding='utf-8') as file:
    file.write(json_content)

print("Archivo modificado exitosamente.")
