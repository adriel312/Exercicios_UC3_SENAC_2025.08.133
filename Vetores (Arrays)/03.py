vetor = [7,6,4,3]

print("Vetor desordenado",vetor)

for i in range(len(vetor)-1):
    for j in range(len(vetor)-1-i):
        if vetor[j+1] < vetor[j]:
            temp = vetor[j]
            vetor[j] = vetor[j+1]
            vetor[j+1] = temp

print("Vetor ordenado",vetor)