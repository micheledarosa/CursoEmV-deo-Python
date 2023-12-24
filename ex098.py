# Faça um programa que tenha uma função chamada
# contador(), que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da
# função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep


def linha():
    print('\033[35m-\033[m' * 20)


def contador(inicio, fim, passo):
    delay = 0.5
    linha()
    sleep(delay)
    if passo == 0:
        print('Passo 0 não é um passo válido, vamos alterá-lo para 1!')
        sleep(delay)
        passo = 1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if passo < 0:
        passo *= -1
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont}', end=' ')
            cont += passo
            sleep(delay)
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont}', end=' ')
            cont -= passo
            sleep(delay)
    print()


contador(1, 10, 1)
contador(10, 0, 2)
linha()
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
