#  Crie um programa que leia o ano de
#  nascimento de sete pessoas. No final, mostre
#  quantas pessoas ainda não atingiram a maioridade
#  e quantas já são maiores.

from datetime import date

maior = 0
menor = 0

for pessoa in range(1, 8):
    anoNasc = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(pessoa)))
    idade = date.today().year - anoNasc

    if idade >= 21:
        maior += 1
    else:
        menor += 1

print('De {} pessoas, {} pessoa(s) atingiram a maioridade e {} pessoa(s) ainda não atingiram.'.format(pessoa, maior,
                                                                                                      menor))
