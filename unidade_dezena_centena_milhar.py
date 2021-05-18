num = int(input('Digite um Numero!'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analizando o Número {}\nUnidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(num, u, d, c, m))
