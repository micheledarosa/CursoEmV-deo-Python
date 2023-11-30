#  Faça um programa que leia o ano de
#  nascimento de um jovem e informe, de acordo
#  com a sua idade, se ele ainda vai se
#  alistar ao serviço militar, se é a hora
#  exata de se alistar ou se já passou do tempo
#  do alistamento. Seu programa também deverá
#  mostrar o tempo que falta ou que passou do
#  prazo.

from datetime import date
print('\033[34m*~\033[m' * 10)
print('\033[34mAlistamento militar\033[m')
print('\033[34m*~\033[m' * 10)

sexo = str(input('Qual é o seu sexo? (F/M) ')).strip()

if sexo == 'F' or sexo == 'f':
    print('O alistamento militar NÃO é obrigatório para mulheres.')
    exit()

nasc = int(input('Qual é o ano de nascimento? '))

atual = date.today().year
idade = atual - nasc

print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} ano(s) para alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade == 18:
    print('Você está na idade exata para alistamento!')
else:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))

