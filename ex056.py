#  Desenvolva um programa que leia o nome,
#  idade e sexo de 4 pessoas. No final do programa,
#  mostre: a média de idade do grupo, qual é o nome
#  do homem mais velho e quantas mulheres têm menos
#  de 20 anos.


somaidade = 0
media = 0
maioridadeh = 0
nomevelho = ''
mulher20 = 0

for p in range(1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (F/M): ')).strip()

    somaidade += idade

    if p == 1 and sexo in 'Mm':
        maioridadeh = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadeh:
        maioridadeh = idade
        nomevelho = nome

    if sexo in 'Ff' and idade < 20:
        mulher20 += 1

media = somaidade / 4

print('A média de idade do grupo é de {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadeh, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulher20))
