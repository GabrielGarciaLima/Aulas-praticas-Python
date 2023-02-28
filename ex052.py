# Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

cont = 0
num = int(input('Digite um número '))
for c in range(1, num+1):
    if num % c == 0:
        print('\033[33m', end='') #formatação
        cont += 1
    else:
        print('\033[31m', end='') #formatação
    print('{} '.format(c), end='') #contagem
print('\n\033[mO número {} foi divisível {} vezes'.format(num, cont))
if cont == 2:
    print('Portanto, ele é um número primo.')
else:
    print('Portanto, ele não é um número primo.')
