"""Exercício Python 67: Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo."""

while True:
    fat2 = 0
    print('-' * 30)
    fat1 = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if fat1 <= 0:
        break
    while fat2 < 10:
        fat2 += 1
        pro = fat1 * fat2
        print(f'{fat1} x {fat2} = {pro}')
print('PROGRAMA ENCERRADO. Volte sempre!')
