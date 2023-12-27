# INTERACTIVE HELP

help(print)  # pode colocar qualquer comando

print(input.__doc__)  # semelhante ao help

# ---------------------------------------------

# DOCSTRINGS


def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Michele da Rosa =)
    """
    c = i
    while c <= f:
        print(f'{c}', end='')
        c += p
    print('Fim!')


contador(2, 10, 2)
help(contador)

# ---------------------------------------------

# PARÂMETROS OPCIONAIS


def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: primeiro valor
    :param b: segundo valor
    :param c: terceiro valor
    Função criada por Michele da Rosa =)
    """
    s = a + b + c
    print(f'A soma vale {s}.')


somar(3, 2, 5)
somar(8, 4)
somar(c=4, b=2)
somar(4)
somar()

# ---------------------------------------------

# ESCOPO DE VARIÁVEIS


def teste():
    """
    x = variável local
    """
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


# Programa principal
n = 2
print(f'No programa principal, n vale {n}')
# print(f'No programa principal, x vale {x}')  # x existe apenas na função teste


def teste2(b=0):
    """
    a, b e c = escopo local
    a vale tanto no local, quanto no global
    """
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5  # escopo global
teste2(2)

# ---------------------------------------------

# RETORNO DE VALORES


def somar2(b=0, c=0, d=0):
    s = b + c + d
    return s


resp = somar2(3, 2, 5)
print(somar2(3, 2, 5))

r1 = somar2(3, 2, 5)
r2 = somar2(2, 2)
r3 = somar2(6)
print(f'Os resultados foram {r1}, {r2} e {r3}.')


# EXEMPLOS


def fatorial(numero=1):
    f = 1
    for c in range(numero, 0, -1):
        f *= c
    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')


def par(valor=0):
    if valor % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')
