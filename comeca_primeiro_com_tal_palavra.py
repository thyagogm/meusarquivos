# Armazenando Valores!
nome_cidade = str(input('Digite o Nome da Cidade!\n'))
# Dividindo as Palavras!
divido = nome_cidade.split()
# Se Santo estiver na Primeira Frase
if 'Santo' in divido[0]:
    print('A Palavra Santo se Encontra na Primeira Frase')
else:
# Caso ao Contrário
    print('A Palavra Santo não se Encontra na Primeira Frase')
