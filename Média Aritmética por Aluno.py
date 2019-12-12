
aluno = input('Nome do Aluno\n\n') #Obtém notas do aluno em ponto flutuante

primeiro = float(input('\nNota no 1° Bimestre\n'))
segundo = float(input('\nNota do 2° Biimestre\n'))
terceiro = float(input('\nNota do 3° Bimestre\n'))
quarto = float(input('\nNota do 4° Bimestre\n'))

soma = primeiro + segundo + terceiro + quarto
media_aluno = soma / 4 #Realiza média aritmética de quatro bimestres
round(media_aluno, 2) #Arredonda para duas casas decimais
print('\nO Aluno' ,aluno, 'alcançou média' ,media_aluno, '\n')
