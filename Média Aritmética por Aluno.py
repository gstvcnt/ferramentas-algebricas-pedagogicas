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
    
    round(media_aluno, 2) #Arredonda, corta, para duas casas decimais
    
    if(media_aluno < media): #Define se o aluno está aprovado ou não
        print('\nREPROVADO: O Aluno' ,aluno, 'alcançou média' ,media_aluno, '\n')
    else:
        print('\nAPROVADO: O Aluno' ,aluno, 'alcançou média' ,media_aluno, '\n')
    if(media_aluno == provavel):
        print('\nOpa! O Aluno' ,aluno, 'ficou por meio ponto:' ,media_aluno, ' que tal tentar um arredondamento?\n')
        
    input('\nPressione ENTER para realizar o cálculo novamente \n')
    os.system('cls' if os.name =='nt' else 'clear') #Limpa terminal
    
    print(aluno, 'alcançou média' ,media_aluno, '\n')
    resultado = aluno,  media_aluno, #String que vai para o arquivo

    arquivo = open("alunos.txt", "a") #Cria arquivo contendo média de todos os alunos
    arquivo.write(str(resultado,))
    arquivo.write('\n\n')
    arquivo.close() #Fecha arquivo
    
    if input == "":
        stop = True
