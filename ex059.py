# Crie um programa que leia dois valores
# e mostre um menu na tela:
#
# [ 1 ] somar
#
# [ 2 ] multiplicar
#
# [ 3 ] maior
#
# [ 4 ] novos números
#
# [ 5 ] sair do programa
#
# Seu programa deverá realizar a operação solicitada
# em cada caso.

valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
print('''----- MENU -----
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa''')

sair = False

while not sair:
    opcao = int(input('Digite a opção desejada: '))
    if opcao == 1:
        soma = valor1 + valor2
        print('{} + {} = {}'.format(valor1, valor2, soma))
    elif opcao == 2:
        mult = valor1 * valor2
        print('{} x {} = {}'.format(valor1, valor2, mult))
    elif opcao == 3:
        if valor1 > valor2:
            print('{} é maior que {}'.format(valor1, valor2))
        elif valor2 > valor1:
            print('{} é maior que {}'.format(valor2, valor1))
        else:
            print('Os valores são iguais!')
    elif opcao == 4:
        print('Digite os novos números desejados')
        valor1 = int(input('Primeiro valor:'))
        valor2 = int(input('Segundo valor: '))
    elif opcao == 5:
        sair = True
        print('Encerrando o programa...')
    else:
        print('Opção inválida! Digite novamente.')
