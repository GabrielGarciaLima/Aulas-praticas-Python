"""Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal."""

num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases abaixo para conversão:')
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
base = int(input('Sua opção: '))
if base == 1:
    print('{} em BINÁRIO é igual a: {}'.format(num, bin(num)[2:]))
elif base == 2:
    print('{} em OCTAL é igual a: {}'.format(num, oct(num)[2:]))
elif base == 3:
    print('{} em HEXADECIMAL é igual a: {}'.format(num, hex(num)[2:]))
else:
    print('OPÇÃO INVÁLIDA! Digite uma opção entre 1 e 3.')
