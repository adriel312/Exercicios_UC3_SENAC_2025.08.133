'''Faça um programa em Python, com uma função que identifica se um número é positivo ou negativo.'''

def eh_negativo(numero):
    if numero>0:
        return("Positivo")
    elif numero<0:
        return("Negativo")
    else:
        return("Neutro")

print(eh_negativo(int(input("Informe um número: "))))