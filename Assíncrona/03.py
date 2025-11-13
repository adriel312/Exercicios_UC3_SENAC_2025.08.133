saque = int(input("Informe o valor do saque: "))

cedulas_100 = saque // 100
resto = saque % 100
print(f"Cédulas de 100: {cedulas_100}")

cedulas_50 = resto // 50
resto = resto % 50
print(f"Cédulas de 50: {cedulas_50}")

cedulas_20 = resto // 20
resto = resto % 20
print(f"Cédulas de 20: {cedulas_20}")

cedulas_10 = resto // 10
resto = resto % 10
print(f"Cédulas de 10: {cedulas_10}")

cedulas_5 = resto // 5
resto = resto % 5
print(f"Cédulas de 5: {cedulas_5}")

cedulas_2 = resto // 2
resto = resto % 2
print(f"Cédulas de 2: {cedulas_2}")

cedulas_1 = resto // 1
resto = resto % 1
print(f"Cédulas de 1: {cedulas_1}")