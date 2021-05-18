frase = str(input('Digite uma Frase: ')).upper().strip()
print('A Letra A Aparece {} vezes na frase.'.format(frase.count('A')))
print('A Primeira letra A Apareceu na posição {}'.format(frase.find('A')+1))
print('A Ultima Letra A Apareceu na posição {}'.format(frase.rfind('A')+1))