#  A Confederação Nacional de Natação
#  precisa de um programa que leia o ano de
#  nascimento de um atleta e mostre sua
#  categoria, de acordo com a idade:
#
# – Até 9 anos: MIRIM
#
# – Até 14 anos: INFANTIL
#
# – Até 19 anos: JÚNIOR
#
# – Até 25 anos: SÊNIOR
#
# – Acima de 25 anos: MASTER

from datetime import date
cores = {'azul': '\033[34m', 'limpa': '\033[m'}

print('{}~{}'.format(cores['azul'], cores['limpa']) * 33)
print('{}Confederação Nacional de Natação{}'.format(cores['azul'], cores['limpa']))
print('{}~{}'.format(cores['azul'], cores['limpa']) * 33)

nasc = int(input('Qual é o ano de nascimento do atleta? '))

atual = date.today().year
idade = atual - nasc

if idade <= 9:
    saldo = 10 - idade
    print('Com {} anos sua categoria atual é {}MIRIM{}.\nEm {} ano(s) sua categoria será {}INFANTIL{}.'.format(idade,
          cores['azul'], cores['limpa'], saldo, cores['azul'], cores['limpa']))
elif idade <= 14:
    saldo = 15 - idade
    print('Com {} anos sua categoria atual é {}INFATIL{}.\nEm {} ano(s) sua categoria será {}JÚNIOR{}.'.format(idade,
          cores['azul'], cores['limpa'], saldo, cores['azul'], cores['limpa']))
elif idade <= 19:
    saldo = 20 - idade
    print('Com {} anos sua categoria atual é {}JÚNIOR{}.\nEm {} ano(s) sua categoria será {}SÊNIOR{}.'.format(idade,
          cores['azul'], cores['limpa'], saldo, cores['azul'], cores['limpa']))
elif idade <= 25:
    print('Com {} anos sua categoria atual é {}SÊNIOR{}.\nApós os 25 anos sua categoria será {}MASTER{}.'.format(idade,
          cores['azul'], cores['limpa'], cores['azul'], cores['limpa']))
else:
    print('Com {} anos sua categoria é {}MASTER{}!'.format(idade, cores['azul'], cores['limpa']))
