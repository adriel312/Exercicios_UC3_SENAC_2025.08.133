frase = input("Digite uma frase: ")
frase_limpa = []
frase_invertida = []

#Limpando a frase de pontuações e espaços
for i in range(len(frase)):
    if frase[i] != " " and frase[i] != "," and frase[i] != "." and frase[i] != "!" and frase[i] != "?" and frase[i] != "-":
        frase_limpa.append(frase[i])

#Invertendo a frase limpa
for i in range(len(frase_limpa) - 1, -1, -1):
    frase_invertida.append(frase_limpa[i])

#Comparando as duas listas
if frase_limpa == frase_invertida:
    print("A frase é um palíndromo!")
else:
    print("A frase não é um palíndromo!")