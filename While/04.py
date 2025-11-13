termo = int(input("Digite o termo da Progressão: "))
razao = int(input("Digite a razão da Progressão: "))
quantidade = int(input("Digite a quantidade de termos: "))
tipo = input("Digite 'A' para PA ou 'G' para PG: ")

i = 0
while quantidade > i:
    print(termo)
    if tipo == 'A':
        termo += razao
    elif tipo == 'G':
        termo *= razao
    i+=1