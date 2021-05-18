# Armazena Dados!
num = int(input('Digite um Numero Qualquer!\n'))
# Descobrindo se é Par ou Impar!
resultado = num % 2
# Se Resultado for igual a 0 Par caso ao Contrario Impar!
if resultado == 0:
    print('O Numero {} é PAR!'.format(num))
else:
    print('O Numero {} é IMPAR'.format(num))