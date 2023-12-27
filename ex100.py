# Faça um programa que tenha uma lista chamada
# números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los
# dentro da lista e a segunda função vai mostrar a soma
# entre todos os valores pares sorteados pela função
# anterior.

from random import randint
from time import sleep
from emoji import emojize


def sorteia(lista):
    print('Sorteando 5 valores...')
    sleep(0.5)
    for n in range(0, 5):
        num = randint(1, 10)
        lista.append(num)
        print(f'{num}', end=' ')
        sleep(0.3)
    print(f'\nColocando os valores na lista...', end='')
    sleep(0.3)
    print(emojize("✔️"))


def soma_par(lista):
    print('Somando os pares:')
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
            print(f'{n} + ', end='')
            sleep(0.3)
    if soma != 0:
        print('\b\b', end='')
    print(f'= {soma}')


numeros = list()
sorteia(numeros)
print('\033[35m-\033[m' * 30)
soma_par(numeros)
