media = int(input('Qual é a média para ser aprovado?\n'))

provavel = (media - 0.5) #Define valor para possível arredondamento com base na média

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
    
    if(media_aluno < media): #Define se o aluno está aprovado ou não
        print('\nREPROVADO: O Aluno' ,aluno, 'alcançou média' ,media_aluno, '\n')
    else:
        print('\nAPROVADO: O Aluno' ,aluno, 'alcançou média' ,media_aluno, '\n')
    if(media_aluno == provavel):
        print('\nOpa! O Aluno' ,aluno, 'ficou por meio ponto:' ,media_aluno, ' que tal tentar um arredondamento?\n')
        
    input('\nPressione ENTER para realizar o cálculo novamente \n')
    os.system('cls' if os.name =='nt' else 'clear') #Limpa terminal, cls em Windows NT caso contrário "clear" em UNIX Like
    
    anterior = aluno #Exibe nome e média do aluno anterior
    print(anterior, 'alcançou média' ,media_aluno, '\n')
    
    if input == "":
        stop = True
