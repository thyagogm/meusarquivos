# Armazenando Valores!
r1 = float(input('Primeiro Segmento!\n'))
r2 = float(input('Segundo Segmento!\n'))
r3 = float(input('Terceiro Segmento!\n'))
# se a soma de dois valores forem menor que um valor forma um triangulo caso contrario não!
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os Segmentos acima podem Forma um Triangulo!')
else:
    print('Os Segmentos acima não podem Forma um Triangulo!')
