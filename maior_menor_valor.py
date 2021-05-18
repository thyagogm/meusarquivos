# Armazenando Dados!
a = int(input('Digite Primeiro Valor!\n'))
b = int(input('Digite Segundo Valor!\n'))
c = int(input('Digite Terceiro Valor!\n'))
# Valores Menores!
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O Menor Valor Digitado Foi {}'.format(menor))
# Valores Maiores!
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O Maior Valor Digitado Foi {}'.format(maior))
'''
# Valores Maiores
if a > b and a > c:
    print('O Maior Valor Digitado foi {}'.format(a))
if b > a and b > c:
    print('O Maior Valor Digitado foi {}'.format(b))
if c > a and c > b:
    print('O Maior Valor Digitado foi {}'.format(c))
# Valores Menores!
if a < b and a < c:
    print('O Menor Valor Digitado foi {}'.format(a))
if b < a and b < c:
    print('O Menor Valor Digitado foi {}'.format(b))
if c < b and c < a:
    print('O Menor Valor Digitado foi {}'.format(c))
'''