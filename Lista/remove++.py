animais = ['tigre', 'tigre', 'tigre', 'tigre', 'tigre', 'tigre', 'tigre', 'tigre', 'tigre']

for i in range(len(animais)):
    if 'tigre' in animais:
        animais.remove('tigre')

print(animais)