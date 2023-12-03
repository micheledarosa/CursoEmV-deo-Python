num = [2, 5, 9, 2, 1]
num[2] = 3
num.append(7)  # adiciona no fim da lista
num.sort()  # coloca em ordem
num.sort(reverse=True)  # ordem decrescente
num.insert(2, 0)  # adiciona o 0 na posição 2
num.pop()  # elimina o último elemento
num.pop(2)  # remove o elemento 2
num.remove(2)  # remove apenas o primeiro elemento 2
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
print(num)
print(f'Essa lista tem {len(num)} elementos.')
# -----------------------------------------------
valores = list()
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v}...', end='')

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!', end='')
print('Cheguei ao final da lista.')

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
# --------------------------------------------------
a = [2, 3, 4, 7]
b = a  # ligação entre as listas
b[2] = 8
print(a)
print(b)
print(f'Lista A: {a}')
print(f'Lista B: {b}')

a = [2, 3, 4, 7]
b = a[:]
# cria uma cópia de a dentro do b, caso haja mudança
# na lista b, não irá alterar a lista a
