import os #Importa módulos para integração com o sistema
print('QUADRADO DA DIFERENÇA (X - A)²')
a = int(input('\nDigite o valor de A\n'))
b = int(input('\nDigite o valor de B\n'))
inicio = a * a #Posteriormente encontrar outra forma de realizar potenciação
meio = 2 * a * b
fim = b * b
core = inicio - meio + fim #Lógica principal da operação
print('O resultado é ',core) #Imprime resultado
input('\nPressione qualquer tecla para sair')
os.system('cls') #Limpa terminal
