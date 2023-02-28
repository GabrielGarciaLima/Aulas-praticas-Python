#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

num = int(input('Digite um número para calcular seu fatorial: '))
cont = num
fat = 1
print('Calculando {}! = '.format(num), end='')
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fat *= cont
    cont -= 1
print('{}'.format(fat))
