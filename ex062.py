"""Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar
mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos."""

print('-=' * 8)
print('GERADOR DE P.A.!')
print('=-' * 8)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da P.A.: '))
termo = primeiro
cont = 1
total = 0
mais_termos = 10
while mais_termos != 0:
    total += mais_termos
    while cont <= total:
        print('{} > '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais_termos = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
