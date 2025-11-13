n = int(input("Digite um número para calcular o fatorial: "))
fatorial = n
while n != 1:
    fatorial *= n-1
    n-=1
print(f"O fatorial é {fatorial}")