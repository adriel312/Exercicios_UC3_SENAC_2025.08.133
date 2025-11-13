'''Faça a sua versão da função len(). Ou seja, crie uma função que recebe uma lista, calcule e retorne o tamanho dessa lista.'''

def tamanho(lista):
    cont = 0
    for i in lista:
        cont+=1
    return cont

print(tamanho([12,12,124,14124,1,412,123,12,3,1,123,12,3,12,31,2,45,1,2,142,12,14,1,2]))