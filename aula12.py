#  estrutura condicional aninhada
nome = str(input('Qual é seu nome? ')).strip()

if nome == 'Michele':
    print('\033[1;45mQue nome bonito!\033[m')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('\033[32mSeu nome é bem popular no Brasil.\033[m')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('\033[4;35mBelo nome feminino\033[m')
else:
    print('Seu nome é bem normal.')
print('\033[33mTenha um bom dia, {}\033[m!'.format(nome))
