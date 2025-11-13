def soma_nat(n):
    if n == 0:
        return 0
    else:
        return n + soma_nat(n-1)

    
print(soma_nat(5))