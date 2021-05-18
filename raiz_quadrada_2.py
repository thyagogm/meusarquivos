# Importação da Biblioteca Math!
from math import sqrt, floor
# Armazena Valores!
num = int(input('Digite um Numero!\n'))
# Somando a Raiz Quadrada com a Função Importada da Biblioteca Math!
raiz = sqrt(num)
# Imprimindo na Tela!
print('raiz de {} é igual a {}\n'.format(num, floor(raiz)))
# Exemplos!
# {:.2f} mostra 3 numeros decimais!
# math.floor(num), arredonda para baixo!
# math.ceil(num), arrendonda para cima!
# Importações Diretas como from math import floor, ceil // não precisa usar math.floor ou math.ceil pode ser direto!
