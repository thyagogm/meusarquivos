# Importação da Função Choice
from random import choice
# Armazenando Valores
a = str(input('Digite 1 Nome!'))
b = str(input('Digite 2 Nome!'))
c = str(input('Digite 3 Nome!'))
d = str(input('Digite 4 Nome!'))
# Utilizando a Função Choice
sorteio = choice([a, b, c, d])
# Imprimindo na Tela
print('O Aluno Sorteado para Apagar o Quadro é = {}'.format(sorteio))