times = (
    'Flamengo', 'Palmeiras', 'Corinthians', 'São Paulo',
    'Santos', 'Grêmio', 'Internacional', 'Cruzeiro',
    'Atlético-MG', 'Botafogo', 'Vasco', 'Chapecoense', 'Fluminense',
    'Bahia', 'Vitória', 'Sport', 'Fortaleza',
    'Ceará', 'Athletico-PR', 'Coritiba', 'Goiás')

print('Lista de times do Brasileirão:')
print('Os 5 primeiros times são:', times[0:5])
print('Os 4 últimos times são:', times[-4:])
print('Os times organizados em ordem alfabética ficam:', sorted(times))
print('O time da Chapecoense está na posição:', times.index('Chapecoense'))