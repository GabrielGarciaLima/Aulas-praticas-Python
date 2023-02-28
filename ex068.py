"""Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias
 consecutivas que ele conquistou no final do jogo."""

from random import randint

print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR!')
print('=-' * 15)

while True:
    meuvalor = int(input('Diga um valor: '))
    seuvalor = randint(0, 10)
    soma = meuvalor + seuvalor
    chute = str(input('Par ou Ímpar? [P/I] '))
    resto = soma % 2

    if resto == 0:
        tipo = 'PAR'
        print('-' * 30)
        print(f'Você jogou {meuvalor} e o computador jogou {seuvalor}. Total de {soma}, deu {tipo}!')
        print('-' * 30)
    else:
        tipo = 'ÍMPAR'
        print('-' * 30)
        print(f'Você jogou {meuvalor} e o computador jogou {seuvalor}. Total de {soma}, deu {tipo}!')
        print('-' * 30)

    if chute == 'p' and tipo == 'PAR':
        print('''Você VENCEU!
Vamos jogar novamente...''')
        print('=-' * 15)
    elif chute == 'i' and tipo == 'ÍMPAR':
        print('''Você VENCEU!
Vamos jogar novamente...''')
    elif chute == 'p' and tipo == 'ÍMPAR':
        print('''Você PERDEU!
GAME OVER! Você venceu x vezes.''')
    elif chute == 'i' and tipo == 'PAR':
        print('''Você PERDEU!
GAME OVER! Você venceu x vezes.''')
