numero = int(input("Digite um número: "))
soma = numero

while numero != 0:
    numero = int(input("Digite o próximo número: "))
    soma += numero

print(f"A soma dos números é {soma}")