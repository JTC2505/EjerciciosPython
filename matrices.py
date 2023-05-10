#inicialice una matriz cuadrada de maximo orden 30 como aparece en el caso a continuacion 
#(orden 5)
#[1, 1, 1, 1, 1]
#[1, 2, 2, 2, 1]
#[1, 2, 3, 2, 1]
#[1, 2, 2, 2, 1]
#[1, 1, 1, 1, 1]
n = 18
matriz = [[0 for x in range(n)] for y in range(n)]

for i in range(n):
    for j in range(n):
        current_value = min(i, j, n-1-i, n-1-j)
        matriz[i][j] = current_value + 1

for row in matriz:
    print(row)