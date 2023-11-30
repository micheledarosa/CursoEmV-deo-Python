frase = '   Curso em Vídeo Python   '
print(frase[::2])
print(frase.upper().count('o'))
print(len(frase))
print(len(frase.strip()))
frase = (frase.replace('Python', 'Android'))
print(frase)
print('Curso' in frase)
print(frase.find('Vídeo'))
print(frase.split())
dividido = frase.split()
print(dividido[2][3])

print("""Nessa aula, vamos aprender operações com String
no Python. As principais operações que vamos aprender são
o Fatiamento de String, Análise com len(), count(), find(),
transformações com replace(), upper(), lower(), capitalize(),
title(), strip(), junção com join().""")

