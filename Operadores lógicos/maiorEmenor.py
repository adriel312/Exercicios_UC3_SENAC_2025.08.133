numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: "))
numero_3 = int(input("Digite o terceiro número: "))

# Determinando o maior número
if numero_1 > numero_2 and numero_1 > numero_3:
    print("O maior número é:",numero_1)
elif numero_2 > numero_1 and numero_2 > numero_3:
    print("O maior número é:",numero_2)
else:
    print("O maior número é:",numero_3)

# Determinando o menor número
if numero_1 < numero_2 and numero_1 < numero_3:
    print("O menor número é:",numero_1)
elif numero_2 < numero_1 and numero_2 < numero_3:
    print("O menor número é:",numero_2)
else:
    print("O menor número é:",numero_3)