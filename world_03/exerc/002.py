times = (
  'Atletico', 'Flamengo', 'Corinthians', 'Chapecoense', 'Palmeiras', 'Fluminense',
  'America-MG', 'SaoPaulo', 'Gremio', 'Vasco da Gama', 'Internacional',
  'Botafogo', 'Sport', 'Recife', 'Cruzeiro', 'Vitoria', 'Santos',
  'Atletico-PR', 'Bahia', 'Ceara', 'Parana'
)

print(f'Lista de times: { times }')
print('-' * 20)
print(f'Os 5 primeiros são: { times[0:5] }')
print('-' * 20)
print(f'Os 4 últimos colocados são: { times[-4:] }')
print('-' * 20)
print(f'Times em ordem alfabética: { sorted(times) }')
print('-' * 20)
print(f'O Chapecoense está na { times.index("Chapecoense") + 1 }ª posição')
