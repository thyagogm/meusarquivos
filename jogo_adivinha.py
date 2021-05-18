# Importando a Função Escolha do Random!
from random import randint
# Importando a Função time Sleep!
from time import sleep
# Criando uma Lista de 0 a 5!
computador = randint(0,5)
# Criando Uma Função de Separação de Linha
def linha():
    print('-=-' * 20)
# Armazenando a Escolha do Usuário
linha()
print('Vou Pensar em um Numero entre 0 a 5. Tente Adivinhar!')
linha()
jogador = int(input('Digite um Numero!\n'))
print('Processando!')
sleep(3)
# se computador for igual Jogador voce ganhou caso ao contrario perdeu!
if computador == jogador:
    linha()
    print('Voce Acertou, O Numero Escolhido é: {}'.format(computador))
    linha()
else:
    linha()
    print('Voce Perdeu!')
    linha()

