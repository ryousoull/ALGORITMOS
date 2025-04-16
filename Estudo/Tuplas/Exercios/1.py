times_classificacao = (
    "Flamengo",
    "Palmeiras",
    "Juventude",
    "Vasco",
    "Fluminense",
    "Internacional",
    "Fortaleza",
    "Ceará",
    "Corinthians",
    "Botafogo",
    "Red Bull Bragantino",
    "Cruzeiro",
    "Grêmio",
    "São Paulo",
    "Bahia",
    "Atlético-MG",
    "Santos",
    "Vitória",
    "Mirassol",
    "Sport"
)

print(f'5 primeiros: {times_classificacao[0:5]}')
print(f'4 ultimos: {times_classificacao[-4:]}')
print(f' Ordem alfabetica: {sorted(times_classificacao)}')
print(f' O flamengo está na posição {times_classificacao.index('Flamengo')+1}')
