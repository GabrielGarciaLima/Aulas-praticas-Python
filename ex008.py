# Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = float(input('Digite a metragem: '))
cm = m * 100
mm = m * 1000
print('{:.2f}m são iguais a {:.0f} centímetros.'.format(m, cm))
print('{:.2f} são iguais a {:.0f} milímetros.'.format(m, mm))
