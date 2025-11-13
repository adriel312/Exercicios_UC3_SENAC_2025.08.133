'''1 - Informar 3 nomes. Mostrar quantas letras "A" e 

"E", possuem.
OBS: O str é um vetor de caracteres.'''

'''nome_1 = input("Informe o primeiro nome: ")
nome_2 = input("Informe o segundo nome: ")
nome_3 = input("Informe o terceiro nome: ")
a=0
e=0
for letra in nome_1:
    if letra == 'a':
        a+=1
    elif letra == 'e':
        e+=1
print(f"O nome {nome_1} possui {a} 'a' e {e} 'e'")
a=0
e=0

for letra in nome_2:
    if letra == 'a':
        a+=1
    elif letra == 'e':
        e+=1
print(f"O nome {nome_2} possui {a} 'a' e {e} 'e'")
a=0
e=0

for letra in nome_3:
    if letra == 'a':
        a+=1
    elif letra == 'e':
        e+=1
print(f"O nome {nome_3} possui {a} 'a' e {e} 'e'")'''

'''nomes = ["adriel","amanda","adriano"]
a=0
e=0
for nome in nomes:
    for letra in nome:
        if letra == 'a':
            a+=1
        elif letra == 'e':
            e+=1
    print(f"O nome {nome} possui {a} 'a' e {e} 'e'.")
    a=0
    e=0'''

nomes = ["adriel","amanda","adriano"]
a=0
e=0
for i in range(len(nomes)):
    for j in range(len(nomes[i])):
        if nomes[i][j] == 'a':
            a+=1
        elif nomes[i][j] == 'e':
            e+=1
    print(f"O nome {nomes[i]} possui {a} 'a' e {e} 'e'.")
    a=0
    e=0