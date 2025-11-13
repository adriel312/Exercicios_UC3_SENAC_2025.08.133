import random
 
numeros_sorteados = []
 
total = 99
 
print("Bingo Maneiro")
while total > 0:
    input("Clique na tecla ENTER para sorteiar um valor.")
   
    valor = random.randrange(1, 100)
    while valor in numeros_sorteados:
        valor = random.randrange(1, 100)
 
    if not valor in numeros_sorteados:
        print(f"Número sorteado {valor}.")
        numeros_sorteados.append(valor)
        total-=1
 
print(numeros_sorteados)