distancia = int(input("Informe a distância em km: "))
combustivel = float(input("Informe o combustível gasto em litros: "))

consumo = distancia / combustivel

print(f"O seu carro faz {consumo:.2f} km/l")