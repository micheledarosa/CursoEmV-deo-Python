# Crie um programa onde o usuário digite
# uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão
# passada está com os parênteses abertos e fechados
# na ordem correta.

exp = str(input('Digite uma expressão: '))
pilha = []
for simb in exp:
    if simb == '(':
        pilha.append('(')  # vai adicionando os parenteses '(' até ele encontrar seu par
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()  # após o parenteses '(' encontrar seu par, remove o último da pilha, até ela estar completa
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
