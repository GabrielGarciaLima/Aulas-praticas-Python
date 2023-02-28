"""Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da
Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time do Internacional."""

times = ('Palmeiras', 'Fluminense', 'Flamengo', 'Corinthians', 'Athletico-PR',
         'Internacional', 'Atlético Mineiro', 'Santos', 'América', 'Goiás',
         'Bragantino', 'Fortaleza', 'São Paulo', 'Botafogo', 'Ceará',
         'Coritiba', 'Cuiabá', 'Avaí', 'Atlético GO', 'Juventede')

print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')

print('-=' * 15)
print(f'Os 5 primeiros são: {times[0:5]}')

print('-=' * 15)
print(f'Os quatro últimos são: {times[-4:]}')

print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')

print('-=' * 15)
print(f'O Internacional está na {times.index("Internacional") + 1}ª posição.')
