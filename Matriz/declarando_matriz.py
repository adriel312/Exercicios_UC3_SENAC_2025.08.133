matriz = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]
matriz = [[0]*4]*4

for i in range(len(matriz)):
    for j in range(len(matriz)):
        matriz[i][j] = int(input(f"Informe o elemento na posição [{i}][{j}]:"))

print(matriz)