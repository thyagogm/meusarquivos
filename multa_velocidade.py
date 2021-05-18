# Armazenando Dados!
spd_car = int(input('Digite a Velocidade do Carro!'))
# Se Velocidade for Maior que 80 então multe! caso ao Contrario não faça nada!
if spd_car > 80:
    multa = (spd_car - 80) * 7
    print('Voce Foi Multado, no Valor de R${}'.format(multa))
else:
    print('Voce Não Foi Multado, Tenha um Bom Dia!')