import os #Módulo sistema
    
stop = False
while not stop:
    
    a = int(input('Digite o valor de A\n'))
    b = int(input('\nDigite o valor de B\n'))
    
    inicio = a * a
    meio = 2 * a * b
    fim = b * b
    
    core = inicio - meio + fim #Lógica central do produto notável
    os.system('cls' if os.name =='nt' else 'clear')
    
    print('RESOLUÇÃO\n')
    print('Valor de A =' ,a)
    print('Valor de B =' ,b, '\n')
    print(a,'²' '+' ' 2' ' x' ,a, 'x' ,b, '+' ,b, '²' '=' ,core)
    print('\nO quadrado da diferença entre' ,a, 'e' ,b, 'é' ,core)
    
    input('\nPressione ENTER para realizar o cálculo novamente')
    os.system('cls' if os.name =='nt' else 'clear')#Limpa terminal para realização de outro cálculo

    if input == "":
        stop = True
