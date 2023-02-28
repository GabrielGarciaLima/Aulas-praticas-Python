# Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('Me diga um número qualquer: '))
resultado = num % 2
if resultado == 1:
    print('O número {} é ÍMPAR!'.format(num))
else:
    print('O número {} é PAR!'.format(num))
