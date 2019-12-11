import os
print('QUADRADO DA DIFERENÇA (X - A)²')
a = int(input('\nDigite o valor de A\n'))
b = int(input('\nDigite o valor de B\n'))
inicio = a * a
meio = 2 * a * b
fim = b * b
core = inicio - meio + fim
print('O resultado é ',core)
input('\nPressione qualquer tecla para sair')
os.system('cls')
