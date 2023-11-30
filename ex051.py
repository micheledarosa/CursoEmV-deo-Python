#  Desenvolva um programa que leia o primeiro
#  termo e a razão de uma PA. No final, mostre os 10
#  primeiros termos dessa progressão.

print('=' * 15)
print('10 TERMOS DA PA')
print('=' * 15)

termo = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
dec = termo + (10 - 1) * raz
for c in range(termo, dec + raz, raz):
    print('{} '.format(c), end='-> ')
print('fim')
