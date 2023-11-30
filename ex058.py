# Melhore o jogo do DESAFIO 28 onde o
# computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até
# acertar, mostrando no final quantos palpites foram
# necessários para vencer.

from random import randint
import emoji

pc = randint(0, 10)

print('-=' * 28)
print('Estou pensando em um número de 0 a 10. Tente adivinhar!')
print('-=' * 28)

chute = int(input('Qual é seu chute? '))
cont = 1

while chute != pc:
    chute = int(input('Número errado! Tente novamente: '))
    cont += 1
print(emoji.emojize('Acertou!! :party_popper: Você deu um total de {} chutes.'.format(cont)))
