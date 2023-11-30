# Refaça o DESAFIO 51, lendo o primeiro termo
# e a razão de uma PA, mostrando os 10 primeiros
# termos da progressão usando a estrutura while.

print('=' * 15)
print('10 TERMOS DA PA')
print('=' * 15)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 1

while cont <= 10:
    print(f'{termo}', end=' → ')
    termo += razao
    cont += 1
print('fim')
