# Crie um programa que leia números inteiros
# pelo teclado. O programa só vai parar quando
# o usuário digitar o valor 999, que é a condição
# de parada. No final, mostre quantos números foram
# digitados e qual foi a soma entre elas (desconsiderando
# o flag).

from time import sleep as pausa
soma = cont = 0

print('\033[34mIniciando o programa...\033[m')
pausa(1.5)
print('Programa iniciado. Digite 999 para encerrar')

while True:
    num = int(input('Digite um número \033[4minteiro\033[m: '))
    if num == 999:
        print('\033[31mEncerrando o programa...\033[m')
        break
    soma += num
    cont += 1

pausa(1.5)
print(f'Foram digitados {cont} números e a soma deles é {soma}.')
