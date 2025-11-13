nomes = []
nota_1 = []
nota_2 = []
media = []
situacao = []

for i in range(6):
    nomes.append(input("Informe seu nome: "))
    nota_1.append(float(input("Informe sua nota 1: ")))
    nota_2.append(float(input("Informe sua nota 2: ")))
    media.append((nota_1[i]+nota_2[i])/2)
    if media[i] >=5:
        situacao.append("Aprovado")
    else:
        situacao.append("Reprovado")

print(nomes)
print(media)
print(situacao)