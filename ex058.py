"""Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai
“pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.
"""

from random import randint
ale = randint(0, 10)
cont = 1
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
palpite = int(input('Qual é seu palpite? '))
while palpite != ale:
    if palpite < ale:
        print('Mais... Tente mais uma vez!')
    if palpite > ale:
        print('Menos... Tente mais uma vez!')
    palpite = int(input('Qual é seu palpite? '))
    cont += 1
print('Meu número era {}!'.format(ale))
print('Acertou com {} tentativas. Parabéns!'.format(cont))
