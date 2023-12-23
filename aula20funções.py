def somar(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


# Programa principal
somar(2, 1)
somar(b=4, a=5)
# -------------------------------------------------------


def contador(*num):  # empacotar = pega todos os parâmetros e "empacota"
    for valor in num:
        print(f'{valor}', end=' ')
    print('FIM!')


def mostrar_tamanho(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')


# Programa principal
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
# --------------------------------------------------------


def dobrar(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


numeros = [6, 3, 9, 1, 0, 2]
dobrar(numeros)
print(numeros)
# --------------------------------------------------------


def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)
