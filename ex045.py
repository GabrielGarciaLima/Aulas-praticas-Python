# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.

from time import sleep
from random import randint
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogada = int(input('Qual é sua jogada? '))
if jogada > 2:
    print('JOGADA INVÁLIDA! Digite um valor entre 0 e 2.')
else:
    sleep(1)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    sleep(1)
    print('-=' * 11)
    lista = ['PEDRA', 'PAPEL', 'TESOURA']
    ale = randint(0, 2)
    print('Computador jogou {}'.format(lista[ale]))
    print('Jogador jogou {}'.format(lista[jogada]))
    print('-=' * 11)
    if (jogada == 0 and ale == 2) or (jogada == 1 and ale == 0) or (jogada == 2 and ale == 1):
        print('JOGADOR VENCE!!!')
    elif (ale == 0 and jogada == 2) or (ale == 1 and jogada == 0) or (ale == 2 and jogada == 1):
        print('COMPUTADOR VENCE!!!')
    else:
        print('EMPATOU! Tente novamente!')
