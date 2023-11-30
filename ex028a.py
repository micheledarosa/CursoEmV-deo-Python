#  Solução do professor

from random import randint
from time import sleep

pc = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
player = int(input('Em que número pensei? '))
print('PROCESSANDO...')
sleep(2)  # você escolhe o tempo que vai ficar em sleep
if player == pc:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(pc, player))
