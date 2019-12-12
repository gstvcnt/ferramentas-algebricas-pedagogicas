stop = False
while not stop:
    import os #Importa Módulo para integração com o Sistema Operacional
    aluno = input('Nome do Aluno\n\n') 

    primeiro = float(input('\nNota no 1° Bimestre\n'))
    segundo = float(input('\nNota no 2° Bimestre\n'))
    terceiro = float(input('\nNota no 3° Bimestre\n'))
    quarto = float(input('\nNota no 4° Bimestre\n'))

    soma = primeiro + segundo + terceiro + quarto
    media_aluno = soma / 4 #Realiza média aritmética de quatro bimestres
    round(media_aluno, 2) #Arredonda para duas casas decimais
    print('\nO Aluno' ,aluno, 'alcançou média' ,media_aluno, '\n')
    input('\nPressione ENTER para realizar o cálculo novamente\n')
    os.system('cls' if os.name =='nt' else 'clear') #Limpa terminal, cls em Windows NT caso contrário "clear" em UNIX Like
    
    if input == "":
        stop = True
