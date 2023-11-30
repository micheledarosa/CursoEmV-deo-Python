#  Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar
#  descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário
#  venceu ou perdeu.

from random import choice
lista = [0, 1, 2, 3, 4, 5]
escolha = choice(lista)
print('--Jogo da adivinhação--')
print('Tente adivinhar o número escolhido entre 0 e 5!')
print('Se você acertar, ganha o jogo!')

num = int(input('Digite o número que você escolheu: '))

if num == escolha:
    print('Parabéns, você ganhou!\nO número escolhido foi {}.'.format(escolha))
else:
    print('Você perdeu :(\nO número escolhido foi {}.'.format(escolha))


