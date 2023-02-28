'''Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre:
1 - Quantas vezes aparece a letra “A”,
2 - Em que posição ela aparece a primeira vez;
3 - Em que posição ela aparece a última vez;'''

frase = str(input('Digite a frase: ')).strip().lower()
frase = frase.replace('á', 'a')
frase = frase.replace('à', 'a')
frase = frase.replace('ã', 'a')
frase = frase.replace('â', 'a')
print('A letra A aparece {} vezes na frase.'.format(frase.count('a')))
print('A primeira letra A aparece na posição {}.'.format(frase.find('a')+1))
print('A última letra A aparece na posição {}.'.format(frase.rfind('a')+1))
