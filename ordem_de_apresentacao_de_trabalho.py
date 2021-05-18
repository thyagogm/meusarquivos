# Importação da Função Shuffle da Biblioteca Random!
from random import shuffle
# Armazenando Valores!
n1 = str(input('Digite o Nome do Primeiro Aluno!\n'))
n2 = str(input('Digite o Nome do Segundo Aluno!\n'))
n3 = str(input('Digite o Nome do Terceiro Aluno!\n'))
n4 = str(input('Digite o Nome do Quarto Aluno!\n'))
# Definindo uam Lista!
lista = [n1, n2, n3, n4]
# Utilizando a Função Shuffle!
rnd = shuffle(lista)
# Imprimindo na Tela!
print('A Ordem de Apresentação do Trabalho é\n{}'.format(lista))
