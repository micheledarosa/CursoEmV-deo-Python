#  Crie um programa que tenha uma dupla
#  totalmente preenchida com uma contagem por extenso,
#  de zero até vinte. Seu programa deverá ler um número
#  pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'quatorze',
        'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))

    while not 0 <= num <= 20:
        print('Número inválido. ', end='')
        num = int(input('Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {cont[num]}')

    continua = ' '
    while continua not in 'SN':
        continua = str(input('Gostaria de ver mais números? [S/N] ')).strip().upper()[0]
    if continua == 'N':
        break
