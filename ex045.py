#  Crie um programa que faça o computador
#  jogar Jokenpô com você.

from random import randint
from emoji import emojize
print('{:=^22}'.format('JOKENPÔ'))
print(emojize('''Escolha uma das opções:
[1] Pedra :raised_fist: 
[2] Papel :raised_hand:
[3] Tesoura :victory_hand:'''))
esc = int(input('1, 2 ou 3? '))

pc = randint(1, 3)

print('=' * 20)
if pc == 1 and esc == 2:
    print('Você ganhou!\nSua escolha: Papel\nPC: Pedra')
elif pc == 1 and esc == 3:
    print('Você perdeu!\nSua escolha: Tesoura\nPC: Pedra')
elif pc == 2 and esc == 1:
    print('Você perdeu!\nSua escolha: Pedra\nPC: Papel')
elif pc == 2 and esc == 3:
    print('Você ganhou!\nSua escolha: Tesoura\nPC: Papel')
elif pc == 3 and esc == 1:
    print('Você ganhou!\nSua escolha: Pedra\nPC: Tesoura')
elif pc == 3 and esc == 2:
    print('Você perdeu!\nSua escolha: Papel\nPC: Tesoura')
elif pc == esc:
    print('Empate!')
else:
    print('Opção inválida')
print('=' * 20)
