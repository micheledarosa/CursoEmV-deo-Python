# Crie um programa que tenha uma função
# fatorial() que receba dois parâmetros: o primeiro
# que indique o número a calcular e outro chamado
# show, que será um valor lógico (opcional) indicando
# se será mostrado ou não na tela o processo de
# cálculo do fatorial.

def calcular_fatorial(numero, show=False):
    """
    -> Calcula o fatorial de um número.
    :param numero: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número.
    """
    f = 1
    for i in range(numero, 0, -1):
        if show:
            print(i, end='')
            if i > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        f *= i
    return f


print(calcular_fatorial(5, True))
help(calcular_fatorial)
