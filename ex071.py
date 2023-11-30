# Crie um programa que simule o funcionamento
# de um caixa eletrônico. No início, pergunte ao usuário
# qual será o valor a ser sacado (número inteiro) e
# o programa vai informar quantas cédulas de cada valor
# serão entregues. OBS:
#
# considere que o caixa possui cédulas de R$50, R$20, R$10
# e R$1.

print('\033[32m-='*15)
print('{:^30}'.format('Caixa Eletrônico'))
print('-='*15)
valor = int(input('\033[mInsira o valor para saque: R$'))
total = valor
ced = 50
qtd_ced = 0

while True:
    if total >= ced:
        total -= ced
        qtd_ced += 1
    else:
        if qtd_ced > 0:
            print(f'Total de {qtd_ced} cédulas de R${ced} sacadas.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        qtd_ced = 0
        if total == 0:
            break

print('\033[32m-=' * 15)
print('\033[mSaque concluído. Volte sempre!')
