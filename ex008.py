#  Escreva um programa que leia um valor em metros e
#  o exiba convertido em centímetros e milímetros.

m = float(input('Digite um valor em metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print('{} metro(s) tem: {} quilômetros, {} hectômetros, {} decâmetros, {} decímetros, {:.0f} centímetros e {:.0f} milímetros.'.format(m, km, hm, dam, dm, cm, mm))
