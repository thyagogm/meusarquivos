# Importando date de datetime
from datetime import date
# Armazenando Valores
ano = int(input('Que ano quer Analisar? Digite 0 Para o ano Atual!'))
# Utilizando a Função DateTime, se ano for igual a 0, verifique o ano atual!
if ano == 0:
    ano = date.today().year
# Se Ano for dividido por 4 e não dividido por 100 ou divido por 400 o ano é bissexto caso contrario não!
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O Ano {} é BISSEXTO!'.format(ano))
else:
    print('O Ano {} não é  BISSEXTO!'.format(ano))
