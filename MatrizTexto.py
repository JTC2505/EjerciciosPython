import numpy as np

# Pedir dimensiones de la matriz
while True:
    try:
        rows = int(input("Introduce el número de filas (máximo 40): "))
        cols = int(input("Introduce el número de columnas (máximo 60): "))
        if rows > 40 or cols > 60:
            print("Dimensiones máximas excedidas. Inténtalo de nuevo.")
            continue
        else:
            break
    except ValueError:
        print("Introduce un número entero.")

# Pedir texto
while True:
    text = input(f"Introduce un texto (máximo {rows*cols} caracteres): ")
    if len(text) > rows*cols:
        print(f"El texto excede el tamaño máximo de la matriz ({rows}*{cols}). Inténtalo de nuevo.")
        continue
    else:
        break

# Crear matriz vacía y llenarla con el texto
matrix = np.empty((rows, cols), dtype='str')
for i in range(rows):
    for j in range(cols):
        if i*cols+j < len(text):
            matrix[i][j] = text[i*cols+j]
        else:
            matrix[i][j] = ' '

# Mostrar matriz
print("\nMatriz resultante:")
for row in matrix:
    print(" ".join(row))

# Calcular frecuencia de cada carácter
char_freq = {}
for char in text:
    if char not in char_freq:
        char_freq[char] = 1
    else:
        char_freq[char] += 1

# Mostrar frecuencia de cada carácter
print("\nFrecuencia de cada carácter:")
for char, freq in char_freq.items():
    print(f"{char}: {freq}")
