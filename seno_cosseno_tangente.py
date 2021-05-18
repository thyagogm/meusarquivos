# Importando a Função de Seno, Cosseno, Tangente e Radius da Biblioteca Math!
from math import sin, cos, tan, radians
# Armazena Valores
ang = float(input('Digite o Ângulo que você Deseja:'))
# Utilizando a Função Seno
sen = sin(radians(ang))
# Imprimindo na Tela
print ('O Ângulo de {} tem o SENO de {:.2f}'.format(ang, sen))
# Utilizando a Função Cosseno
cos = cos (radians(ang))
# Imprimindo na Tela
print('O Ângulo de {} tem o COSSENO de {:.2f}'.format(ang, cos))
# Utilizando a Função Tangente
tan = tan(radians(ang))
# Imprimindo na Tela
print('O Ângulo de {} tem o TANGENTE de {:.2f}'.format(ang, tan))
