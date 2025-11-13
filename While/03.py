nota = float(input("Digite uma nota: "))
soma = nota
conta_notas = 1
while nota>=0:
    nota = float(input("Digite uma nota: "))
    while nota>10:
        print("Nota inválida! Tente novamente.")
        nota = float(input("Digite uma nota: "))
    if nota>0:
        soma += nota
        conta_notas += 1
media = soma/conta_notas
print(f"A média das notas é {media}")