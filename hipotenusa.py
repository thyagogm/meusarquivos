# Importando hypot da Biblioteca Math!
from math import hypot
# Armazenando Valores!
co = float(input('Comprimento do Cateto oposto!\n'))
ca = float(input('Comprimento do Cateto adjacente!\n'))
# Utilizando a Função hypot que soma a Hipotenusa!
hi = hypot(co, ca)
# Imprimindo na Tela!
print('A Hipotenusa vai Medir {:.2f}'.format(hi))

# Fazendo sem Importação!
'''
co = float(input('Comprimento do Cateto oposto!\n'))
ca = float(input('Comprimento do Cateto adjacente!\n'))
hi = (co ** 2 + ca ** 2 ) ** (1/2)
print('A Hipotenusa vai medir {:.2f}'.format(hi))
'''