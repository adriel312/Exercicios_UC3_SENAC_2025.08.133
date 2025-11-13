x = int(input("Digite o valor de X: "))
y = int(input("Digite o valor de Y: "))

resultado = x

for i in range(y - 1):
    resultado = resultado * x
print(resultado)