#  TUPLAS

# 1 - Tuplas são IMUTÁVEIS.

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')  # pode-se colocar sem parênteses
print(lanche[1:3])  # apenas suco e pizza
print(lanche[2:])  # elemento 2 até o final
print(lanche[:2])  # do início até o elemento 2 (ignora o 2)
print(lanche[-2])  # de trás pra frente (ignora o 2)
print(len(lanche))
print(sorted(lanche))  # coloca em ordem

for comida in lanche:
    print(f'Eu vou comer {comida}')  # caso não precise de posição

# for pos, comida in enumerate(lanche):
#    print(f'Eu vou comer {comida} na posição {pos}')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.count(5))  # mostra qntas vzs aparece o nº
print(c.index(8))  # mostra em qual posição está o nº, pega a primeira ocorrência

pessoa = ('Michele', 29, 'F')
print(pessoa)
del(pessoa)  # apaga a tupla inteira, n eh possível apagar apenas 1 item
