# Armazena Valores
largura = int(input('Digite a Largura!\n'))
comprimento = int(input('Digite a Comprimento!\n'))
tinta = int(input('Digite Quantos M² Faz por Litro\n'))
# Soma
quadrados = (comprimento * largura)
# Resultado
print('Largura = {}m\nComprimento = {}m\nTotal de M² = {}M²\nVocê Precisa de = {}L de Tinta'.format(largura, comprimento, quadrados, quadrados / tinta))
