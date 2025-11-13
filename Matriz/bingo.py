import random

cartela = []
numeros_usados = []

for i in range(5):
    linha = []
    for j in range(5):
        numero = random.randrange(1, 99)
        linha.append(numero)
        if not numero in numeros_usados:
            numeros_usados.append(numero)
    cartela.append(linha)

'''
Algoritmo para substituir valores gerados repetidos
Ele pega os valores armazenados no vetor numero_usados e verifica
se ele possui menos de 25 elementos.
Se possuir ele vai gerar novos valores repetidos e adicionar no vetor, após
isso pego os valores no vetor numeros_usados e adiciono em cada indice da matriz
cartela
'''
if len(numeros_usados) < 25:
    total = 25-len(numeros_usados)
    while total > 0:
        valor = random.randrange(1, 99)
        if not valor in numeros_usados:
            numeros_usados.append(valor)
            n = 0
            for i in range(5):
                for j in range(5):
                    cartela[i][j] = numeros_usados[n]
                    if n < len(numeros_usados)-1:
                        n+=1
            total-=1
        else:
            valor = random.randrange(1, 99)


for i in range(5):
    for j in range(5):
        print(cartela[i][j], end=" ")
    print("")