# Desenvolva um programa que leia quatro valores
# pelo teclado e guarde-os em uma tupla. No final,
# mostre:
#
# A) Quantas vezes apareceu o valor 9.
#
# B) Em que posição foi digitado o primeiro valor 3.
#
# C) Quais foram os números pares.

valores_escolhidos = ()
numero_par = ()

for c in range(1, 5):
    valor = int(input(f'Digite o {c}º valor: '))
    valores_escolhidos += (valor,)
    if valor % 2 == 0:
        numero_par += (valor,)

print('*~' * 10 + '*')
print(f'Valores digitados: {valores_escolhidos}')
print('*~' * 10 + '*')
print(f'O número 9 apareceu {valores_escolhidos.count(9)} vez(es).')
print('*~' * 10 + '*')
print(f'O valor 3 apareceu a primeira vez na posição {valores_escolhidos.index(3)+1}')
print('*~' * 10 + '*')
print(f'Os números pares digitados são: {numero_par}')
