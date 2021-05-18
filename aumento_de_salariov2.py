# Armazena Valores!
salario = float(input('Digite o Valor do Salario!'))
if salario <= 1250:
    aumento = salario + (salario * 15 / 100)
else:
    aumento = salario + (salario * 10 / 100)
print('o Valor do seu Salário é = R${}\nCom o Aumento do Salário é = R${}'.format(salario, aumento))
