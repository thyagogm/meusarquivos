# Armazenando Valores/ Ignorando espaços/ Dividindo as Palavras
nome = str(input('Digite o Seu Nome Completo!')).strip().split()
# Imprimindo na tela e Mostrando o Primeiro Nome!
print('Seu Primeiro nome é {}'.format(nome[0]))
# Imprimindo na Tela e Mostrando o Ultimo Nome!
print('Seu Ultimo Nome é {}'.format(nome[len(nome)-1]))
