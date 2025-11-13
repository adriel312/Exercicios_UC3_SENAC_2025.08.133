lista = []

for i in range(1,11,1):
    lista.append(int(input(f"Digite o {i}º valor: ")))

menor = lista[0]
for i in range(len(lista)):
    if lista[i] < menor:
        menor = lista[i]

print(f"O menor valor é {menor}")