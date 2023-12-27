#  Crie um programa que tenha uma função
#  chamada voto() que vai receber como parâmetro o
#  ano de nascimento de uma pessoa, retornando um
#  valor literal indicando se uma pessoa tem voto
#  NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(ano):
    from datetime import datetime
    idade = datetime.now().year - ano

    if 16 <= idade < 18 or idade >= 70:
        return f'Com {idade} anos: "Voto OPCIONAL"'
    elif 18 <= idade < 70:
        return f'Com {idade} anos: "Voto OBRIGATÓRIO"'
    else:
        return f'Com {idade} anos: "Voto NEGADO"'


ano_nasc = int(input("Em que ano você nasceu? "))
print(voto(ano_nasc))
