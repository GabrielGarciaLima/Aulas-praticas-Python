"""Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso."""

from time import sleep
v1 = float(input('Primeiro valor: '))
v2 = float(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair''')
    opcao = int(input('>>>>> Qual é a sua opção? '))
    if opcao == 1:
        soma = v1 + v2
        print('A soma entre {} + {} é {}'.format(v1, v2, soma))
        print('=-' * 10)
    elif opcao == 2:
        mult = v1 * v2
        print('A multiplicação entre {} * {} é {}'.format(v1, v2, mult))
        print('=-' * 10)
    elif opcao == 3:
        if v1 < v2:
            print('Entre {} e {}, o maior valor é {}'.format(v1, v2, v2))
        if v1 > v2:
            print('Entre {} e {}, o maior valor é {}'.format(v1, v2, v1))
            print('=-' * 10)
    elif opcao == 4:
        print('Informe os números novamente:')
        v1 = float(input('Primeiro valor: '))
        v2 = float(input('Segundo valor: '))
    elif opcao > 5:
        print('Opção inválida! Tente novamente')
        print('=-' * 10)
    sleep(1)
if opcao == 5:
    print('Finalizando...')
    print('=-' * 10)
    sleep(1)
    print('Fim do programa. Volte sempre!')
