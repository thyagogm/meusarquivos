# Armazena Valores
carteira = float(input('Digite o Valor em sua Carteira!'))
# Cotação do Dólar
dolar = float(input('Digite o Valor da Cotação do Dólar!'))
# Resultado
print('Seu Saldo é de = R${}\nVocê Pode Comprar até {}USD'.format(carteira, carteira/dolar))
