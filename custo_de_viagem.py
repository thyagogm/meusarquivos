# Armazenando Valores!
distancia = float(input('Distancia da Sua Viagem!\n'))
# Imprimindo na Tela!
print('Voce esta preste a comecar uma viagem de {} KM'.format(distancia))
# Simplificado, se distancia for menor ou igual 200 cobre distancia por 0.50 c_aso ao contrario 0.45
valor = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('O Preco da sua passagem sera de R${:.2f}'.format(valor))
# Normal
'''if distancia <= 200:
    valor = distancia * 0.50
else:
    valor = distancia * 0.45
'''