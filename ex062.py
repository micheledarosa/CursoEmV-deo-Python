# Melhore o DESAFIO 61, perguntando para
# o usuário se ele quer mostrar mais alguns
# termos. O programa encerrará quando ele disser
# que quer mostrar 0 termos.

print('=' * 15)
print('10 TERMOS DA PA')
print('=' * 15)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo}', end=' → ')
        termo += razao
        cont += 1
    print('pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados')
