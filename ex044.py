"""Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros"""

print('{:=^40}'.format(' LOJAS DO GABE '))
compras = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO:
[1] à vista em dinheiro/cheque
[2] à vista no cartão de crédito
[3] 2x no cartão de crédito
[4] 3x ou mais no cartão de crédito''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = compras - (compras * 10 / 100)
    print('Sua compra de R${:.2f} vai custar {:.2f} no final.'.format(compras, total))
elif opcao == 2:
    total = compras - (compras * 5 / 100)
    print('Sua compra de R${:.2f} vai custar {:.2f} no final.'.format(compras, total))
elif opcao == 3:
    total = compras
    parcela = compras / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS.'.format(parcela))
    print('Sua compra de R${:.2f} vai custar {:.2f} no final.'.format(compras, compras))
elif opcao == 4:
    juros = compras + (compras * 20 / 100)
    parcelas = int(input('Quantas parcelas? '))
    parcela = juros / parcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(parcelas, parcela))
    print('Sua compra de R${:.2f} vai custar {:.2f} no final.'.format(compras, juros))
else:
    print('OPÇÃO INVÁLIDA! Digite uma opção entre 1 e 4.')
