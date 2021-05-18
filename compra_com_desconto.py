# Armazena Valores
produto = float(input('Digite o Valor do Produto!\n'))
porcentagem = float(input('Digite A Porcentagem do Desconto!\n'))
desconto = (porcentagem * produto) / 100
# Resultado
print('O Valor da sua Compra é = R${}\nCom Desconto o Valor da sua Compra é = R${}'.format(produto, produto - desconto))