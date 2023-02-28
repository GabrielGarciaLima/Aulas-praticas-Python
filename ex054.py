"""Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores."""

menor = 0
maior = 0
from datetime import date
anoatu = date.today().year
for pes in range(1, 8):
    anonas = int(input('Em que ano a {}ª pessoa nasceu: '.format(pes)))
    if anoatu - anonas < 21:
        menor += 1
    elif anoatu - anonas >= 21:
        maior += 1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(maior))
print('E também tivemos {} pessoas menor de idade.'.format(menor))
