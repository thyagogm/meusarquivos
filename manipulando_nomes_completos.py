# Armazena Valores / Ignora os Espaços!
nome = str(input('Digite o Seu Nome!\n')).strip()
# Nome em Maiúscula
print(nome.upper())
# Nome em Minuscula
print(nome.lower())
# Lê
print('O Nome Completo tem o total de: {} Letras'.format(len(nome) - nome.count(' ')))
print('O Primeiro nome tem o total de: {} Letras'.format(nome.find(' ')))